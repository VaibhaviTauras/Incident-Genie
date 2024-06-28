from fastapi.responses import JSONResponse
from service_layer.translate import translate_text


def success_response(data: dict, message: str = 'success', meta_code: int = 200, **extra):
    res = {
        "data": data,
        "meta": {
            "message": message,
            "code": meta_code,
            **extra
        }
    }
    return res


def error_response(message: str, meta_code: int = 400, status_code: int = 200, data: dict | None = None, language_id: int = 1):
    if data is None:
        data = {}
    res = {
        "data": data,
        "meta": {
            "message": translate_text(message, language_id),
            "code": meta_code
        }
    }
    return JSONResponse(
        res,
        status_code=status_code
    )
