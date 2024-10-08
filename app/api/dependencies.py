import httpx
from core.settings import settings
from fastapi import HTTPException, status

__USER_LOGIN_API = settings.Ouranos.user_authentication_origin + "/auth/login"


async def get_ouranos_access_token():
    headers = {
        "Content-Type": "application/json",
        "apiKey": settings.Ouranos.api_key,
    }

    json = {
        "operatorAccountId": settings.Ouranos.operator_account_id,
        "accountPassword": settings.Ouranos.account_password,
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(__USER_LOGIN_API, headers=headers, json=json)
            response.raise_for_status()
        except httpx.HTTPStatusError as err:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail={
                    "message": "Cannot authenticate user in Ouranos",
                    "error": err.response.json(),
                },
            )

    result = response.json()
    return result["accessToken"]
