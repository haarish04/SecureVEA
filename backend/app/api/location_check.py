from fastapi import APIRouter, HTTPException
import httpx
from app.schema.model import LocationVerifyRequest
from app.config.secrets import secrets

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
        response.raise_for_status()
        return response.json()

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
        response.raise_for_status()
        return response.json()