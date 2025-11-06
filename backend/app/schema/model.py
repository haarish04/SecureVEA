from pydantic import BaseModel

class CallForwardingRequest(BaseModel):
    phoneNumber: str

class UnconditionalCallForwardingRequest(BaseModel):
    phoneNumber: str

class DeviceSwapRetrieveDateRequest(BaseModel):
	phoneNumber: str

class DeviceSwapRequest(BaseModel):
	phoneNumber: str
	maxAge: int = 120

class SimSwapRetrieveDateRequest(BaseModel):
	phoneNumber: str

class SimSwapCheckRequest(BaseModel):
	phoneNumber: str
	maxAge: int = 240

class RiskCheckRequest(BaseModel):
    phoneNumber: str
    reason: str = None

class LocationRetrieveRequest(BaseModel):
	phoneNumber: str
	maxAge: int = 120

class LocationVerifyRequest(BaseModel):
    device_phoneNumber: str
    area_center_latitude: float
    area_center_longitude: float
    area_radius: int