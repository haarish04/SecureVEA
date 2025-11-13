import json
import httpx
from app.config.secrets import secrets

async def call_llm_for_risk_analysis(context: dict):
    """
    Sends fraud signals context to Gemini LLM and expects a response with a fraud likelihood score and rationale.
    """
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent"
    api_key = secrets.GOOGLE_API_KEY
    headers = {
        "x-goog-api-key": api_key,
        "Content-Type": "application/json"
    }
   
    prompt = (
        "You are an expert fraud risk analyst. "
        "Given the following telecom account signals and risk indicators (in JSON), "
        "analyze how likely this scenario reflects SIM swap fraud, device swap, or account hijack. "
        "Give a fraud likelihood score from 0 (no risk) to 10 (highest risk) "
        "and a short rationale for your score. \n"
        "Here is the input data:\n\n"
        f"{json.dumps(context, indent=2)}\n"
        "Respond in this exact JSON format:\n"
        "{\n"
        "  \"fraud_score\": <number from 0 to 10>,\n"
        "  \"rationale\": <short explanation>\n"
        "}"
    )
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }
    async with httpx.AsyncClient(verify=secrets.CERTS_PATH) as client:
        response = await client.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
