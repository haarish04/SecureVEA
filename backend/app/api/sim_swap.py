from fastapi import APIRouter, HTTPException
import httpx
from app.schema.model import SimSwapCheckRequest, SimSwapRetrieveDateRequest
from app.config.secrets import secrets
 
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
        response.raise_for_status()
        return response.json()

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
        response.raise_for_status()
        return response.json()