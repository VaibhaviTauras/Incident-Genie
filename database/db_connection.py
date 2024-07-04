from config.config import settings
from service_layer.database import DatabaseManager
from service_layer.unit_of_work import SqlAlchemyUnitOfWork


class DatabaseConnector:
    @classmethod
    async def create_connection(cls, username, password, hostname, port, db_name):
        db_manager = DatabaseManager(username=username,
                                     password=password,
                                     hostname=hostname,
                                     port=port,
                                     db_name=db_name)
        session, engine = db_manager.db_session()
        return session, engine
    
    
# master db connection
async def get_db():
    session, engine = await DatabaseConnector.create_connection(
        username=settings.MASTER_DB_USER,
        password=settings.MASTER_DB_PASSWORD,
        hostname=settings.MASTER_DB_HOSTNAME,
        port=settings.MASTER_DB_PORT,
        db_name=settings.MASTER_DB_NAME
    )
    with SqlAlchemyUnitOfWork(session) as db:
        yield db

# service db connection
async def get_service_db_session(service_db_credentials):
        session, engine = await DatabaseConnector.create_connection(
            username=service_db_credentials.username,
            password=service_db_credentials.password,
            hostname=service_db_credentials.hostname,
            port=service_db_credentials.port,
            db_name=service_db_credentials.db_name
        )
        with SqlAlchemyUnitOfWork(session) as db:
            return db


#use this to connect your other service db.
#service_db_session = get_service_db_session(subsidary_database_details)