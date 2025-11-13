from fastapi import APIRouter, HTTPException
import httpx
from app.schema.model import UnconditionalCallForwardingRequest, CallForwardingRequest
from app.config.secrets import secrets
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=2, max=10), retry=retry_if_exception_type(httpx.HTTPError))
async def unconditional_call_forwarding_api(phone_number: str) -> dict:
    url = "https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/call-forwarding-signal/call-forwarding-signal/v0.3/call-forwardings"
    payload = {"phoneNumber": phone_number}
    headers = {
        "x-rapidapi-key": secrets.RAPIDAPI_KEY,
        "x-rapidapi-host": secrets.RAPIDAPI_HOST,
        "x-correlator": "b4333c46-49c0-4f62-80d7-f0ef930f1c46"
    }
    async with httpx.AsyncClient(verify=secrets.CERTS_PATH) as client:
        response = await client.post(url, json=payload, headers=headers)
        if response.status_code != 200:
            raise httpx.HTTPError(f"Non-200 response: {response.status_code}")
        return response.json()


@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=2, max=10), retry=retry_if_exception_type(httpx.HTTPError))
async def call_forwarding_api(phone_number: str) -> dict:
    url = "https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/call-forwarding-signal/call-forwarding-signal/v0.3/unconditional-call-forwardings"
    payload = {"phoneNumber": phone_number}
    headers = {
        "x-rapidapi-key": secrets.RAPIDAPI_KEY,
        "x-rapidapi-host": secrets.RAPIDAPI_HOST,
        "x-correlator": "b4333c46-49c0-4f62-80d7-f0ef930f1c46"
    }
    async with httpx.AsyncClient(verify=secrets.CERTS_PATH) as client:
        response = await client.post(url, json=payload, headers=headers)
        if response.status_code != 200:
            raise httpx.HTTPError(f"Non-200 response: {response.status_code}")
        return response.json()