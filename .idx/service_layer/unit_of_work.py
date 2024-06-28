from contextlib import contextmanager

from logger.logger import logger


@contextmanager
def SqlAlchemyUnitOfWork(session):
    db = session()
    try:
        yield db
    except Exception as e:
        db.rollback()
        logger.error(f"Exception raised in DB session:{str(e)}. Transaction rolled back.")
        raise Exception(str(e))
    finally:
        db.close()
