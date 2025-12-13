import uuid
from sqlalchemy import Column,String,DateTime,JSON
from datetime import datetime
from app.db.base import Base

class Session(Base):
    __tablename__="sessions"

    id = Column(String, primary_key=True, default=lambda:str(uuid.uuid4()))
    preferred_styles=Column(JSON,nullable=False)
    created_at=Column(DateTime,default=datetime.utcnow)