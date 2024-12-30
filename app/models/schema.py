from pydantic import BaseModel,Field
from typing import List, Optional, Union
from fastapi import UploadFile

class ApiResponse(BaseModel):
    status_code: int
    message: str
    data: Union[List[dict], dict, None]

class PostSchema(BaseModel):
    likes: int = Field(default=0)  # Default value is 0
    shares: int = Field(default=0)  # Default value is 0
    postTypes: str  # e.g., "carousel", "reels", "static"
    comments: Optional[Union[List[str], dict, str]] = Field(default_factory=list)  # Optional, defaults to an empty list
    username: str

