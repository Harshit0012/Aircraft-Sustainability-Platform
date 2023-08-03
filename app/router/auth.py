from fastapi import APIRouter, Depends, HTTPException, status
from ..database import get_db, Session, func
from .. import models, schemas, utils, oauth2

router = APIRouter(tags=['AUTHENTICATE'])

@router.post('/{opt}/signup')
def signUp(opt: str, info: schemas.signUp ,db: Session = Depends(get_db)):
    roleMap = {'m': models.Manufacturer, 'a': models.Airline, 'r': models.RFacility}
    mod = roleMap.get(opt)

    if mod is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invaid role")

    if opt=='r':
        info = schemas.signUpFacility(user_id=info.user_id, pwd=info.pwd)
    
    # srch_usr = db.query(mod).filter(func.binary(mod.user_id)==info.user_id).first()
    srch_usr = db.query(mod).filter(mod.user_id==info.user_id).first()

    if srch_usr is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email is already registered")
    else:
        hashed_pwd = utils.hash(info.pwd)
        info.pwd = hashed_pwd 
        new_usr = mod(**info.dict())
        db.add(new_usr)
        db.commit()
        db.refresh(new_usr)
        user = schemas.RSignUp(user_id=info.user_id, role=opt)
        if(opt!='r'): user.company = info.company
        return user

@router.post('/{opt}/signin')
def signIn(opt: str, info: schemas.signIn, db:Session = Depends(get_db)):
    roleMap = {'m': models.Manufacturer, 'a': models.Airline, 'r': models.RFacility}
    mod = roleMap.get(opt)

    if mod is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invaid role")

    user_id = info.user_id
    pwd = info.pwd
        
    # search = db.query(mod).filter(func.binary(mod.user_id)==user_id).first()
    search = db.query(mod).filter(mod.user_id==user_id).first()

    if search is None: raise HTTPException(status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION, detail='invalid credentials')
    else:
        if not utils.verify(pwd, search.pwd):  raise HTTPException(status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION, detail='invalid credentials')
        else: 
            data = {
                'user_id': user_id,
                'opt':opt
            }
            token = oauth2.create_access_token(data)
            return {'token':token}