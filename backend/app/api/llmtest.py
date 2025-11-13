from google import genai
from fastapi import APIRouter, HTTPException
import httpx
from app.config.secrets import secrets

async def testllm():
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent"
    api_key = secrets.GOOGLE_API_KEY 
    headers = {
        "x-goog-api-key": api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": "How does AI work? Explain VERY SHORTLY"
                    }
                ]
            }
        ]
    }
    async with httpx.AsyncClient(verify=secrets.CERTS_PATH) as client:
        response = await client.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
 
