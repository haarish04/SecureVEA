from fastapi import APIRouter, HTTPException
import httpx
from app.schema.model import SimSwapCheckRequest, SimSwapRetrieveDateRequest
from app.config.secrets import secrets
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
 

# Retry up to 5 times with exponential backoff if not 200 or network error
@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=2, max=10), retry=retry_if_exception_type(httpx.HTTPError))
async def sim_swap_check_api(phone_number: str, max_age: int = 240):
    url = "https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/sim-swap/sim-swap/v0/check"
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
async def sim_swap_retrieve_date_api(phone_number: str):
    url = "https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/sim-swap/sim-swap/v0/retrieve-date"
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