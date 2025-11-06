from fastapi import APIRouter, HTTPException
from app.schema.model import (
    SimSwapCheckRequest, SimSwapRetrieveDateRequest,
    DeviceSwapRequest, DeviceSwapRetrieveDateRequest,
    CallForwardingRequest, UnconditionalCallForwardingRequest,
    RiskCheckRequest, LocationVerifyRequest, LocationRetrieveRequest
)

from app.api.sim_swap import sim_swap_check_api, sim_swap_retrieve_date_api
from app.api.device_swap import device_swap_api, device_swap_date_api
from app.api.call_forwarding import call_forwarding_api, unconditional_call_forwarding_api
from app.api.location_check import location_retrieval_api, location_verification_api
from app.api.risk_check import risk_check_api

router = APIRouter()

@router.post("/sim-swap/check")
async def sim_swap_check(data: SimSwapCheckRequest):
    try:
        return await sim_swap_check_api(data.phoneNumber, data.maxAge)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/sim-swap/retrieve-date")
async def sim_swap_retrieve_date(data: SimSwapRetrieveDateRequest):
    try:
        return await sim_swap_retrieve_date_api(data.phoneNumber)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/device-swap/check")
async def device_swap(data: DeviceSwapRequest):
    try:
        return await device_swap_api(data.phoneNumber, data.maxAge)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/device-swap/retrieve-date")
async def device_retrieve_date(data: DeviceSwapRetrieveDateRequest):
    try:
        return await device_swap_date_api(data.phoneNumber)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/call-forwarding")
async def call_forwarding(data: CallForwardingRequest):
    try:
        return await call_forwarding_api(data.phoneNumber)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/call-forwarding/unconditional")
async def unconditional_call_forwarding(data: UnconditionalCallForwardingRequest):
    try:
        return await unconditional_call_forwarding_api(data.phoneNumber)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/location/retrieve")
async def location_retrieval(data: LocationRetrieveRequest):
    try:
        return await location_retrieval_api(data.phoneNumber, data.maxAge)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/location/verify")
async def location_verification(data: LocationVerifyRequest):
    try:
        return await location_verification_api(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# @router.post("/risk-profile")
# async def risk(data: RiskCheckRequest):
#     try:
#         result = await risk_check_api(data)
#         return result
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


# @app.post("/transcribe-file")        
# async def speech_to_text(file: UploadFile = File(...)):
#     # Save the uploaded file temporarily
#     with httpx.Client(verify=secrets.CERTS_PATH) as client:

#         upload_resp = client.post(
#             "https://api.assemblyai.com/v2/upload",
#             headers={"authorization": ASSEMBLYAI_API_KEY},
#             content=file.file
#         )
#         upload_resp.raise_for_status()
#         audio_url = upload_resp.json()["upload_url"]

       
#         transcript_resp = client.post(
#             "https://api.assemblyai.com/v2/transcript",
#             headers={
#                 "authorization": ASSEMBLYAI_API_KEY,
#                 "content-type": "application/json"
#             },
#             json={
#                 "audio_url": audio_url,
#                 "speaker_labels": True,
#                 "format_text": True,
#                 "punctuate": True,
#                 "speech_model": "universal",
#                 "language_code": "en_us"
#             }
#         )
#         transcript_resp.raise_for_status()
#         transcript_id = transcript_resp.json()["id"]
#         polling_url = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"

       
#         while True:
#             poll_resp = client.get(polling_url, headers={"authorization": ASSEMBLYAI_API_KEY})
#             poll_resp.raise_for_status()
#             data = poll_resp.json()
#             if data["status"] == "completed":
#                 return JSONResponse(content={"text": data["text"], "id": transcript_id})
#             elif data["status"] == "error":
#                 raise HTTPException(status_code=500, detail=str(data["error"]))
#             else:
#                 await asyncio.sleep(3)

