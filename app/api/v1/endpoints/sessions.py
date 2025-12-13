from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session
from app.schemas.session import SessionCreate,SessionResponse
from app.db.models.session import Session
from app.db.base import SessionLocal

router=APIRouter(tags=["sessions"])

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/sessions",response_model=SessionResponse)
def create_session(payload:SessionCreate, db:Session=Depends(get_db)):
    session=Session(preferred_styles=payload.preferred_styles)
    db.add(session)
    db.commit()
    db.refresh(session)

    return{"session_id":session.id}
