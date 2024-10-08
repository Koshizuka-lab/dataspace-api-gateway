from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class OuranosSettings(BaseModel):
    data_transaction_origin: str = "http://localhost:8080"
    data_transaction_api_prefix: str = "/api/v1"
    user_authentication_origin: str = "http://localhost:8081"
    api_key: str = "DefaultApiKey"
    operator_account_id: str = "test_operator"
    account_password: str = "password"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_nested_delimiter="__")

    # Ouranos Environment
    Ouranos: OuranosSettings = OuranosSettings()


settings = Settings()
