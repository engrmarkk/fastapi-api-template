from database import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    DateTime,
    Float,
    Text,
    Enum as SQLAlchemyEnum,
)
# from sqlalchemy.orm import relationship
# from helpers import generate_uuid, format_datetime
from datetime import datetime, timedelta
from enum import Enum
from models.model_similarities import TimestampMixin, UUIDPrimaryKeyMixin


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"


class Users(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    __tablename__ = "users"
    email = Column(String(50), unique=True)
    password = Column(Text)
    verify_email = Column(Boolean, default=False)
