from fastapi import FastAPI
from app.routes import router
from app.schema.model import UnconditionalCallForwardingRequest
from app.config.corsconfig import get_cors_config
from fastapi.middleware.cors import CORSMiddleware

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = FastAPI()
app.include_router(router)

cors_config = get_cors_config()

app.add_middleware(CORSMiddleware, **cors_config)