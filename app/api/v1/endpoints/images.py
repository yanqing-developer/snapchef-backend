from fastapi import APIRouter,UploadFile,File,HTTPException,Depends
from sqlalchemy.orm import Session
from typing import List

router=APIRouter(tags=["images"])
@router.post("/sessions/{session_id}/images")
async def upload_images(session_id:str,images:List[UploadFile]=File(...)):
    return{"ok":True,"count":len(images)}