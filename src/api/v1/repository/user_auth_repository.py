from sqlalchemy.orm import Session
from logger.logger import logger, log_format
from src.api.v1.models.user_models.user import Question, \
    Organisation


async def add_organisation_questions(db: Session, organisation_name: str, question_list: list):
    """
    add user in user_subsidiary
    @param: db_session
    @param: organisation_id
    @param: question_list
    @return: questions
    """
    try:
        logger.info(log_format(msg=f"add_organisation_questions"))

        organisation = Organisation(
            name=organisation_name,
            workflow=str(question_list)
        )
        db.add(organisation)
        db.commit()  # Commit to generate the ID for the organisation
        db.refresh(organisation)  # Refresh to get the new ID assigned to the organisation

        # Save the questions to the database
        for q in question_list:
            db_question = Question(
                organisation_id=organisation.id,  # Use the newly assigned organisation ID
                question=q["question"],
                response_type=q["response_type"],
                question_type=q["question_type"],
                options=q["options"]
            )
            db.add(db_question)
        db.commit()
    except Exception as e:
        logger.error(log_format(msg=f"Error: add_user_subsidiary: {str(e)}."))
        raise Exception("Something went wrong")
    else:
        return question_list


async def get_organisation_questions(db: Session):
    """
    add user in user_subsidiary
    @param: db_session
    @param: organisation_id
    @param: question_list
    @return: questions
    """
    try:
        logger.info(log_format(msg=f"get_organisation_questions"))
        organisation = db.query(Organisation).all()

    except Exception as e:
        logger.error(log_format(msg=f"Error: add_user_subsidiary: {str(e)}."))
        raise Exception("Something went wrong")
    else:
        return organisation
