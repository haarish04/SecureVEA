from fastapi import APIRouter, HTTPException
import httpx
from app.schema.model import UnconditionalCallForwardingRequest, CallForwardingRequest
from app.config.secrets import secrets

# router = APIRouter()

# @router.post("/unconditional")
# async def unconditional_call_forwarding(data: UnconditionalCallForwardingRequest):
#     url = "https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/call-forwarding-signal/call-forwarding-signal/v0.3/unconditional-call-forwardings"
#     payload = {"phoneNumber": data.phoneNumber}
#     headers = {
#         "x-rapidapi-key": secrets.RAPIDAPI_KEY,
#         "x-rapidapi-host": secrets.RAPIDAPI_HOST,
#         "x-correlator": "b4333c46-49c0-4f62-80d7-f0ef930f1c46"
#     }
#     try:
#         async with httpx.AsyncClient(verify=secrets.CERTS_PATH) as client:
#             response = await client.post(url, json=payload, headers=headers)
#             response.raise_for_status()
#         return response.json()
#     except httpx.HTTPError as e:
#         raise HTTPException(status_code=500, detail=str(e))


# @router.post("/")
# async def call_forwarding(data: CallForwardingRequest):
#     url = "https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/call-forwarding-signal/call-forwarding-signal/v0.3/call-forwardings"
#     payload = {"phoneNumber": data.phoneNumber}
#     headers = {
#         "x-rapidapi-key": secrets.RAPIDAPI_KEY,
#         "x-rapidapi-host": secrets.RAPIDAPI_HOST,
#         "x-correlator": "b4333c46-49c0-4f62-80d7-f0ef930f1c46"
#     }
#     try:
#         async with httpx.AsyncClient(verify=secrets.CERTS_PATH) as client:
#             response = await client.post(url, json=payload, headers=headers)
#             response.raise_for_status()
#         return response.json()
#     except httpx.HTTPError as e:
#         raise HTTPException(status_code=500, detail=str(e))


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
        response.raise_for_status()
        return response.json()


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
        response.raise_for_status()
        return response.json()