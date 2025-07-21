from models import (
    Users
)
from helpers import hash_password
from environmentals import SESSION_EXPIRES, DEFAULT_PASSWORD
from datetime import datetime, timedelta
from fastapi import Request, HTTPException
from logger import logger
from sqlalchemy import func, desc


async def email_exists(db, email: str):
    return db.query(Users).filter(Users.email.ilike(email)).first()


def get_user_id_from_request(request: Request):
    user_id = request.state.user_id
    logger.info(f"user_id: {user_id}")
    if not user_id:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return user_id
