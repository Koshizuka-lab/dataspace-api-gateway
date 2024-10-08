from typing import Literal

import httpx
from api.dependencies import get_ouranos_access_token
from core.settings import settings
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()

__DATA_TRANSPORT_API = (
    settings.Ouranos.data_transaction_origin + settings.Ouranos.data_transaction_api_prefix + "/datatransport"
)


@router.get("/datatransport")
async def fetch_cfp(
    dataTarget: Literal["cfp", "parts"] = "cfp",
    traceIds: str | None = None,
    access_token: str = Depends(get_ouranos_access_token),
):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
        "apiKey": settings.Ouranos.api_key,
    }

    params = {
        "dataTarget": dataTarget,
        "traceIds": traceIds,
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(__DATA_TRANSPORT_API, headers=headers, params=params)
            response.raise_for_status()
        except httpx.HTTPStatusError as err:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={
                    "message": "Cannot fetch data from Ouranos",
                    "error": err.response.json(),
                },
            )

    return response.json()
