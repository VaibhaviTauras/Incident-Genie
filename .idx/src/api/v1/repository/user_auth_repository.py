from uuid import UUID
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta

from config.config import settings
from logger.logger import logger, log_format
from src.api.v1.models.user_models.user import UserMaster, UserSubsidiary, UsersProfileConnection
from src.api.v1.models.domain_models.domain import DomainMaster, SubsidiaryDomain
from src.api.v1.models.organization_models.organization import OrganizationMaster
from src.api.v1.models.subsidiary_models.subsidiary import SubsidiaryMaster, SubsidiaryDetails
from src.api.v1.models.user_validation_models.user_validation import UserValidation, EmailTemplateMaster
from src.api.v1.constants.constants import DEV_ENV
from src.api.v1.constants.db_constants import FREEMIUM_WS_ID


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

