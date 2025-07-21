from pydantic import BaseModel, EmailStr, field_serializer, HttpUrl
from typing import Optional
from datetime import datetime


class ShowUserSchema(BaseModel):
    email: Optional[EmailStr]
