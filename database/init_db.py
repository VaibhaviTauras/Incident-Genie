from config.config import settings
from logger.logger import logger, log_format
from database.db_connection import DatabaseConnector


async def init_db():
    try:
        _, engine = await DatabaseConnector.create_connection(
            username=settings.MASTER_DB_USER,
            password=settings.MASTER_DB_PASSWORD,
            hostname=settings.MASTER_DB_HOSTNAME,
            port=settings.MASTER_DB_PORT,
            db_name=settings.MASTER_DB_NAME
        )

        logger.info(log_format(msg="database loading..."))

        try:
            conn = engine.raw_connection()
            cursor = conn.cursor()
            cursor.execute('INSERT into language_master (id) Values (1);')
        except:
            return "Initial database already setup."
        else:
            cursor.execute('DELETE FROM language_master WHERE id=1;')
            cursor.execute('ALTER SEQUENCE language_master_id_seq RESTART WITH 1;')
            conn.commit()

        csv_file_path_language_master = 'seeder/language_master.csv'
        with open(csv_file_path_language_master, 'r', encoding='utf-8') as f:
            conn = engine.raw_connection()
            cursor = conn.cursor()
            query = 'COPY language_master(isocode,name,native_name,is_active) FROM STDIN WITH ' \
                    '(FORMAT CSV, HEADER)'
            cursor.copy_expert(query, f)
            conn.commit()
        logger.info(log_format(msg="language_master database setup success."))

        csv_file_path_terms_conditions = 'seeder/terms_conditions.csv'
        with open(csv_file_path_terms_conditions, 'r', encoding='utf-8') as f:
            conn = engine.raw_connection()
            cursor = conn.cursor()
            query = 'COPY terms_conditions(language_master_id,file_location,is_active) FROM STDIN WITH ' \
                    '(FORMAT CSV, HEADER)'
            cursor.copy_expert(query, f)
            conn.commit()
        logger.info(log_format(msg="terms_conditions database setup success."))

        csv_file_path_email_template_master = 'seeder/email_template_master.csv'
        with open(csv_file_path_email_template_master, 'r', encoding='utf-8') as f:
            conn = engine.raw_connection()
            cursor = conn.cursor()
            query = 'COPY email_template_master(language_master_id,template,is_active) FROM STDIN WITH ' \
                    '(FORMAT CSV, HEADER)'
            cursor.copy_expert(query, f)
            conn.commit()
        logger.info(log_format(msg="email_template_master database setup success."))

        csv_file_path_workspace_master = 'seeder/workspace_master.csv'
        with open(csv_file_path_workspace_master, 'r', encoding='utf-8') as f:
            conn = engine.raw_connection()
            cursor = conn.cursor()
            query = 'COPY workspace_master(name,is_active) FROM STDIN WITH ' \
                    '(FORMAT CSV, HEADER)'
            cursor.copy_expert(query, f)
            conn.commit()
        logger.info(log_format(msg="workspace_master database setup success."))

        csv_file_path_service_master = 'seeder/service_master.csv'
        with open(csv_file_path_service_master, 'r', encoding='utf-8') as f:
            conn = engine.raw_connection()
            cursor = conn.cursor()
            query = 'COPY service_master(name,is_active) FROM STDIN WITH ' \
                    '(FORMAT CSV, HEADER)'
            cursor.copy_expert(query, f)
            conn.commit()
        logger.info(log_format(msg="service_master database setup success."))

        csv_file_path_subsidiary_theme_json = 'seeder/subsidiary_theme_json.csv'
        with open(csv_file_path_subsidiary_theme_json, 'r', encoding='utf-8') as f:
            conn = engine.raw_connection()
            cursor = conn.cursor()
            query = 'COPY subsidiary_theme_json(theme_json,is_active) FROM STDIN WITH ' \
                    '(FORMAT CSV, HEADER)'
            cursor.copy_expert(query, f)
            conn.commit()
        logger.info(log_format(msg="subsidiary_theme_json database setup success."))

        csv_file_path_domain_master = 'seeder/domain_master.csv'
        with open(csv_file_path_domain_master, 'r', encoding='utf-8') as f:
            conn = engine.raw_connection()
            cursor = conn.cursor()
            query = 'COPY domain_master(access_domain,is_active) FROM STDIN WITH ' \
                    '(FORMAT CSV, HEADER)'
            cursor.copy_expert(query, f)
            conn.commit()
        logger.info(log_format(msg="domain_master database setup success."))

        csv_file_path_organization_master = 'seeder/organization_master.csv'
        with open(csv_file_path_organization_master, 'r', encoding='utf-8') as f:
            conn = engine.raw_connection()
            cursor = conn.cursor()
            query = 'COPY organization_master(id,name,domain_org_name,has_paid_subsidiary,is_active) FROM STDIN WITH ' \
                    '(FORMAT CSV, HEADER)'
            cursor.copy_expert(query, f)
            conn.commit()
        logger.info(log_format(msg="organization_master database setup success."))

        csv_file_path_subsidiary_master = 'seeder/subsidiary_master.csv'
        with open(csv_file_path_subsidiary_master, 'r', encoding='utf-8') as f:
            conn = engine.raw_connection()
            cursor = conn.cursor()
            query = 'COPY subsidiary_master(id,organization_master_id,name,workspace_name,is_global,is_default,is_active) FROM STDIN WITH ' \
                    '(FORMAT CSV, HEADER)'
            cursor.copy_expert(query, f)
            conn.commit()
        logger.info(log_format(msg="subsidiary_master database setup success."))

        csv_file_path_subsidiary_details = 'seeder/subsidiary_details.csv'
        with open(csv_file_path_subsidiary_details, 'r', encoding='utf-8') as f:
            conn = engine.raw_connection()
            cursor = conn.cursor()
            query = 'COPY subsidiary_details(id,subsidiary_master_id,workspace_master_id,default_language_id,is_active) FROM STDIN WITH ' \
                    '(FORMAT CSV, HEADER)'
            cursor.copy_expert(query, f)
            conn.commit()
        logger.info(log_format(msg="subsidiary_details database setup success."))

        csv_file_path_subsidiary_domain = 'seeder/subsidiary_domain.csv'
        with open(csv_file_path_subsidiary_domain, 'r', encoding='utf-8') as f:
            conn = engine.raw_connection()
            cursor = conn.cursor()
            query = 'COPY subsidiary_domain(subsidiary_master_id,domain_master_id,is_active) FROM STDIN WITH ' \
                    '(FORMAT CSV, HEADER)'
            cursor.copy_expert(query, f)
            conn.commit()
        logger.info(log_format(msg="subsidiary_domain database setup success."))

        csv_file_path_chatbot_status_master = 'seeder/chatbot_status_master.csv'
        with open(csv_file_path_chatbot_status_master, 'r', encoding='utf-8') as f:
            conn = engine.raw_connection()
            cursor = conn.cursor()
            query = 'COPY chatbot_status_master(name,is_active) FROM STDIN WITH ' \
                    '(FORMAT CSV, HEADER)'
            cursor.copy_expert(query, f)
            conn.commit()
        logger.info(log_format(msg="chatbot_status_master database setup success."))

        csv_file_path_chatbot_master = 'seeder/chatbot_master.csv'
        with open(csv_file_path_chatbot_master, 'r', encoding='utf-8') as f:
            conn = engine.raw_connection()
            cursor = conn.cursor()
            query = 'COPY chatbot_master(id,chatbot_name,chatbot_email,chatbot_index,chatbot_icon,chatbot_status_master_id,enabled_by_default,is_active) FROM STDIN WITH ' \
                    '(FORMAT CSV, HEADER)'
            cursor.copy_expert(query, f)
            conn.commit()
        logger.info(log_format(msg="chatbot_master database setup success."))

        csv_file_path_chatbot_supported_language = 'seeder/chatbot_supported_language.csv'
        with open(csv_file_path_chatbot_supported_language, 'r', encoding='utf-8') as f:
            conn = engine.raw_connection()
            cursor = conn.cursor()
            query = 'COPY chatbot_supported_language(chatbot_master_id,language_master_id,is_active) FROM STDIN WITH ' \
                    '(FORMAT CSV, HEADER)'
            cursor.copy_expert(query, f)
            conn.commit()
        logger.info(log_format(msg="chatbot_supported_language database setup success."))

        csv_file_path_subsidiary_chatbot_language = 'seeder/subsidiary_chatbot_language.csv'
        with open(csv_file_path_subsidiary_chatbot_language, 'r', encoding='utf-8') as f:
            conn = engine.raw_connection()
            cursor = conn.cursor()
            query = 'COPY subsidiary_chatbot_language(subsidiary_master_id,chatbot_supported_language_id,is_active) FROM STDIN WITH ' \
                    '(FORMAT CSV, HEADER)'
            cursor.copy_expert(query, f)
            conn.commit()
        logger.info(log_format(msg="subsidiary_chatbot_language database setup success."))

        csv_file_path_chatbot_utterance = 'seeder/chatbot_utterance.csv'
        with open(csv_file_path_chatbot_utterance, 'r', encoding='utf-8') as f:
            conn = engine.raw_connection()
            cursor = conn.cursor()
            query = 'COPY chatbot_utterance(utterance,language_master_id,chatbot_master_id,is_active) FROM STDIN WITH ' \
                    '(FORMAT CSV, HEADER)'
            cursor.copy_expert(query, f)
            conn.commit()
        logger.info(log_format(msg="chatbot_utterance database setup success."))

        csv_file_path_chatbot_name_language = 'seeder/chatbot_name_language.csv'
        with open(csv_file_path_chatbot_name_language, 'r', encoding='utf-8') as f:
            conn = engine.raw_connection()
            cursor = conn.cursor()
            query = 'COPY chatbot_name_language(chatbot_name,chatbot_master_id,language_master_id,is_active) FROM STDIN WITH ' \
                    '(FORMAT CSV, HEADER)'
            cursor.copy_expert(query, f)
            conn.commit()
        logger.info(log_format(msg="chatbot_name_language database setup success."))

        logger.info(log_format(msg="initial database setup success."))
        return "Initial database setup."
    except Exception as e:
        logger.error(log_format(msg=f"Error: init_db {str(e)}"))
        raise Exception("Initial database not setup.")