from api import ouranos
from core.settings import settings
from fastapi import APIRouter

api_router = APIRouter()

# Ouranos API
api_router.include_router(
    ouranos.router, prefix=f"/ouranos{settings.Ouranos.data_transaction_api_prefix}", tags=["Ouranos"]
)
