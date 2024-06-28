from sqlalchemy.orm import Session
from fastapi import APIRouter, status, Request, Depends

from database.db_connection import get_db
from logger.logger import logger, log_format
from set_response.response import error_response, success_response
# from src.api.v1.models.language_models.language import SubsidiaryChatbotLanguage, ChatbotSupportedLanguage


router = APIRouter(prefix="/test-view")


@router.post("/test", summary="test.", status_code=status.HTTP_200_OK)
async def test_data(request: Request, input: str):
    """
    test
    """
    logger.info(log_format(msg="inside function: test.", request=f'{request.__dict__}'))
    try:
        results = get_user_master_id_by_email(email = vaibhavi.thakker@navatechgroup.com)
        # response = success_response(results)
    except Exception as e:
        logger.error(log_format(msg=f"Error: test_data: {e}"))
        return error_response(str(e))
    else:
        return success_response(results)

async def get_user_master_id_by_email(db: Session, email: str):
    """
    get user master id by email
    @param: db_session
    @param: email
    @return: user_master_id
    """
    try:
        logger.info(log_format(msg=f"get user master id by email: {email}."))
        user_master_tuple = db.query(UserMaster).filter(UserMaster.email == email.lower()).first()
        if user_master_tuple:
            user_master_tuple.is_active = True
            db.commit()
            db.refresh(user_master_tuple)
            user_master_id = user_master_tuple.id
        else:
            user_master_id = None
            
    except Exception as e:
        logger.error(log_format(msg=f"Error: get_user_master_id_by_email: {str(e)}."))
        raise Exception("Something went wrong")
    else:
        return user_master_id