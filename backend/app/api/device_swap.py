from fastapi import APIRouter, HTTPException
import httpx
from app.schema.model import DeviceSwapRequest, DeviceSwapRetrieveDateRequest
from app.config.secrets import secrets

@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=2, max=10), retry=retry_if_exception_type(httpx.HTTPError))
async def device_swap_api(phone_number: str, max_age: int = 120):
    url = "https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/device-swap/device-swap/v1/check"
    payload = {"phoneNumber": phone_number, "maxAge": max_age}
    headers = {
        "x-rapidapi-key": secrets.RAPIDAPI_KEY,
        "x-rapidapi-host": secrets.RAPIDAPI_HOST,
        "Content-Type": "application/json"
    }
    async with httpx.AsyncClient(verify=secrets.CERTS_PATH) as client:
        response = await client.post(url, json=payload, headers=headers)
        if response.status_code != 200:
            raise httpx.HTTPError(f"Non-200 response: {response.status_code}")
        return response.json()

@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=2, max=10), retry=retry_if_exception_type(httpx.HTTPError))
async def device_swap_date_api(phone_number: str):
    url = "https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/device-swap/device-swap/v1/retrieve-date"
    payload = {"phoneNumber": phone_number}
    headers = {
        "x-rapidapi-key": secrets.RAPIDAPI_KEY,
        "x-rapidapi-host": secrets.RAPIDAPI_HOST,
        "Content-Type": "application/json"
    }
    async with httpx.AsyncClient(verify=secrets.CERTS_PATH) as client:
        response = await client.post(url, json=payload, headers=headers)
        if response.status_code != 200:
            raise httpx.HTTPError(f"Non-200 response: {response.status_code}")
        return response.json()