from fastapi import APIRouter, HTTPException
import httpx
from app.schema.model import DeviceSwapRequest, DeviceSwapRetrieveDateRequest
from app.config.secrets import secrets

# router = APIRouter()

# @router.post("/")
# async def device_check(data: DeviceCheckRequest):
#     url = "https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/device-swap/device-swap/v1/check"
#     payload = {
#         "phoneNumber": data.phoneNumber,
#         "maxAge": data.maxAge
#     }
#     headers = {
#         "x-rapidapi-key": secrets.RAPIDAPI_KEY,
#         "x-rapidapi-host": secrets.RAPIDAPI_HOST,
#         "Content-Type": "application/json"
#     }
#     try:
#         async with httpx.AsyncClient(verify=secrets.CERTS_PATH) as client:
#             response = await client.post(url, json=payload, headers=headers)
#             response.raise_for_status()
#         return response.json()
#     except httpx.HTTPError as e:
#         raise HTTPException(status_code=500, detail=str(e))


# @router.post("/retrieve-date")
# async def retrieve_date(data: RetrieveDateRequest):
#     url = "https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/device-swap/device-swap/v1/retrieve-date"
#     payload = {"phoneNumber": data.phoneNumber}
#     headers = {
#         "x-rapidapi-key": secrets.RAPIDAPI_KEY,
#         "x-rapidapi-host": secrets.RAPIDAPI_HOST,
#         "Content-Type": "application/json"
#     }
#     try:
#         async with httpx.AsyncClient(verify=secrets.CERTS_PATH) as client:
#             response = await client.post(url, json=payload, headers=headers)
#             response.raise_for_status()
#         return response.json()
#     except httpx.HTTPError as e:
#         raise HTTPException(status_code=500, detail=str(e))

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
        response.raise_for_status()
        return response.json()

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
        response.raise_for_status()
        return response.json()