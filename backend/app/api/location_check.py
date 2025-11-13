from fastapi import APIRouter, HTTPException
import httpx
from app.schema.model import LocationVerifyRequest
from app.config.secrets import secrets
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=2, max=10), retry=retry_if_exception_type(httpx.HTTPError))
async def location_retrieval_api(phone_number: str, max_age: int = 120):
    url = "https://network-as-code.p-eu.rapidapi.com/location-retrieval/v0/retrieve"
    payload = {
        "device":{
            "phoneNumber": phone_number, 
            },

        "maxAge": max_age

        }
        
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
async def location_verification_api(data: LocationVerifyRequest):
    url = "https://network-as-code.p-eu.rapidapi.com/location-verification/v1/verify"
    payload = {
    "device": {
        "phoneNumber": data.device_phoneNumber
    },
    "area": {
        "areaType": "CIRCLE",
        "center": {
            "latitude": data.area_center_latitude,
            "longitude": data.area_center_longitude
        },
        "radius": data.area_radius
    }
}

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