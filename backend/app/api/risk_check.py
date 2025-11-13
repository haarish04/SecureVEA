from fastapi import APIRouter, HTTPException
import httpx

from app.schema.model import RiskCheckRequest
from app.config.secrets import secrets
from app.api.sim_swap import sim_swap_check_api, sim_swap_retrieve_date_api
from app.api.device_swap import device_swap_api, device_swap_date_api
from app.api.call_forwarding import call_forwarding_api, unconditional_call_forwarding_api
from app.api.risk_analyzer import call_llm_for_risk_analysis

async def risk_check_api(data: RiskCheckRequest):
    results = {}
    results['device_swap_date'] = "NA"
    results['sim_swap_date'] = "NA"

    try:
        results['device_swap'] = await device_swap_api(data.phoneNumber, max_age=120)
    except Exception as e:
        results['device_swap'] = str(e)

    try:
        results['sim_swap'] = await sim_swap_check_api(data.phoneNumber, max_age=240)
    except Exception as e:
        results['sim_swap'] = str(e)

    try:
        results['call_forwarding'] = await call_forwarding_api(data.phoneNumber)
    except Exception as e:
        results['call_forwarding'] = str(e)

    device_swap_result = results.get('device_swap', {})
    sim_swap_result = results.get('sim_swap', {})
    call_forwarding_result = results.get('call_forwarding', [])

    #Retrieve status in case the result from API changes or additional data is sent
    
    device_swap_status = device_swap_result.get('swapped', True) if isinstance(device_swap_result, dict) else True
    sim_swap_status = sim_swap_result.get('swapped', True) if isinstance(sim_swap_result, dict) else True
    call_forwarding_status = call_forwarding_result.get('active', True) if isinstance(call_forwarding_result, dict) else True

    #Retrieve date of swap if detected

    if device_swap_status is True:
        try:
            device_swap_date = await device_swap_date_api(data.phoneNumber)
            results['device_swap_date'] = device_swap_date
        except Exception as e:
            results['device_swap_date'] = str(e)

    if sim_swap_status is True:
            try:
                sim_swap_date = await sim_swap_retrieve_date_api(data.phoneNumber)
                results['sim_swap_date'] = sim_swap_date
            except Exception as e:
                results['sim_swap_date'] = str(e)

    device_msg = "No Device swap detected" if not device_swap_status else "Device swap detected"
    sim_msg = "No SIM swap detected" if not sim_swap_status else "SIM swap detected"
    call_forwarding_status_msg = "Call forwarding active" if call_forwarding_status else "No Call forwarding setup"


    if not device_swap_status and not sim_swap_status and call_forwarding_status:
        status = "Trusted"
    elif device_swap_status and sim_swap_status and not call_forwarding_status:
        status = "Fraud"
    else:
        status = "Spam or Warning"
    
    llm_context = {
        "device_swap": results.get("device_swap"),
        "device_swap_date": results.get("device_swap_date"),
        "sim_swap": results.get("sim_swap"),
        "sim_swap_date": results.get("sim_swap_date"),
        "call_forwarding": results.get("call_forwarding")
    }

    try:
        llm_response = await call_llm_for_risk_analysis(llm_context)
        llm_content = llm_response["candidates"][0]["content"]["parts"][0]["text"]
        llm_json = {}
        # Try to parse the LLM response as JSON
        try:
            llm_json = json.loads(llm_content)
        except Exception:
            llm_json = {"fraud_score": None, "rationale": llm_content}
    except Exception as e:
        llm_json = {"fraud_score": None, "rationale": f"LLM error: {str(e)}"}

    return {
        "status": status,
        "device_swap_result": device_msg,
        "device_swap_date": results.get('device_swap_date'),
        "sim_swap_result": sim_msg,
        "sim_swap_date": results.get('sim_swap_date'),
        "call_forwarding_result": call_forwarding_status_msg,
        "llm_fraud_score": llm_json.get("fraud_score"),
        "llm_rationale": llm_json.get("rationale"),
    }

    # return {
    #     "status": status,
    #     "device_swap_result": device_msg,
    #     "device_swap_date": results.get('device_swap_date'),
    #     "sim_swap_result": sim_msg,
    #     "sim_swap_date": results.get('sim_swap_date'),
    #     "call_forwarding_result": call_forwarding_status_msg,
    # }
