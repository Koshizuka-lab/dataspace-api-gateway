from typing import Literal

from pydantic import BaseModel


class DataTransportParams(BaseModel):
    dataTarget: Literal["cfp", "parts"] = "cfp"
    traceIds: str
