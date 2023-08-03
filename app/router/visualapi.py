from typing import Optional, List
from fastapi import APIRouter, Depends, HTTPException, status
from ..database import get_db, Session, func
from .. import models, schemas, utils, oauth2

router = APIRouter(tags=['VISUAL'])

@router.get('/vis/{option}/',response_model=List[schemas.fullDet])
def repurpose(option:str, db: Session = Depends(get_db), 
              user: oauth2.get_current_user = Depends(),
              limit: Optional[int] = 10, 
              offset: Optional[int] = 0):
    roleMap = {'m': models.Manufacturer, 'a': models.Airline, 'r': models.RFacility}
   
    user_id  = user.dict().get('user_id')
    role  = user.dict().get('opt')
    mod = roleMap.get(role)

    if mod is None:
        raise HTTPException(status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION, detail='invalid token')
    
    search = db.query(mod).filter(mod.user_id==user_id).first()
    if search is None:
        raise HTTPException(status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION, detail='invalid token')

    results = HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid option")
    if option=='repurpose':
        results = db.query(models.recycleEffortScore).order_by(models.recycleEffortScore.effort).offset(offset).limit(limit).all()
    elif option=='recycle':
        results = db.query(models.recycleEffortScore).order_by(models.recycleEffortScore.effort.desc()).offset(offset).limit(limit).all()

    lst = []
    for row in results:
        row_dict = row.__dict__
        lst.append(row_dict['pid'])
    
    parts = []
    for pid in lst:
        part = db.query(models.PartTable).filter(models.PartTable.pid==pid).first()
        parts.append(part)

    return parts

@router.get('/vis/supervis', response_model=schemas.superVis)
def supervis(db: Session = Depends(get_db)):

    repurposeMaterial = db.query(
        models.PartTable.mat_comp,
        func.count(models.PartTable.mat_comp)
    ).join(
        models.recycleEffortScore,
        models.PartTable.pid == models.recycleEffortScore.pid
    ).filter(
        models.recycleEffortScore.effort >= 50
    ).group_by(
        models.PartTable.mat_comp
    ).all()
    
    recycleMaterial = db.query(
        models.PartTable.mat_comp,
        func.count(models.PartTable.mat_comp)
    ).join(
        models.recycleEffortScore,
        models.PartTable.pid == models.recycleEffortScore.pid
    ).filter(
        models.recycleEffortScore.effort < 50
    ).group_by(
        models.PartTable.mat_comp
    ).all()

    result = schemas.superVis(recycleMat=recycleMaterial, repurposeMat=repurposeMaterial)
    return result