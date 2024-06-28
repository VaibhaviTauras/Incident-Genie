import logging
from datetime import datetime
from fastapi import Request


# Create a custom logging handler
class UTCFormatter(logging.Formatter):
    # Set the timestamp to the current UTC time 
    converter = datetime.utcfromtimestamp
    def formatTime(self, record, datefmt=None):
        current_utc_time = self.converter(record.created)
        # Format the time in ISO 8601 UTC format
        formatted_time = current_utc_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        return formatted_time


def get_logger():
    """
    function to get log service
    @return: logger
    """
    try:
        from config.config import settings
        service_name = settings.SERVICE_NAME
    except:
        service_name = 'util'

    logger = logging.getLogger(service_name)
    formatter = 'timestamp:%(asctime)s, name:%(name)s, loglevel:%(levelname)s, module:%(module)s, file:%(filename)s, line:%(lineno)d, %(message)s'
    logger.setLevel(logging.DEBUG)
    log_service_handler = logging.StreamHandler()
    log_service_handler.setFormatter(UTCFormatter(formatter))
    logger.addHandler(log_service_handler)
    return logger


logger = get_logger()


util_version = "1.2.3"


def log_format(sid: str | None = None, uid: str | None = None,
                msg: str | None = None, screen: str | None = None, 
                request: Request | None = None, response: str | None = None,
                client: str | None = "n-bkend"):
    """
    This function collect all default log info and return the message string which will be store in log file
    @param: sid - subsidiary_master_id (ex. UUID) 
    @param: uid - user_id (ex. UUID)
    @param: msg
    @param: screen (ex. login, registration) for m-app 
    @param: request
    @param: response
    @param: client (ex. n-mapp, n-bkend)
    @return: logging message string
    """
    if client != "n-bkend":
        message = f"client:{client}, subsidiaryId:{sid}, userId:{uid}, screen:{screen}, request:{request}, response:{response}, msg:{msg}"
    else:
        message = f"client:{client}, subsidiaryId:{sid}, userId:{uid}, request:{request}, response:{response}, msg:{msg}"
    return message