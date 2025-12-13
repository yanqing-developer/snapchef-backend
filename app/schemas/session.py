from pydantic import BaseModel
from typing import List


class SessionCreate(BaseModel):
    preferred_styles: List[str]

class SessionResponse(BaseModel):
    session_id: str