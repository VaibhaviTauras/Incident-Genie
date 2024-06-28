import os
from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from fastapi_restful.timing import add_timing_middleware

from config.config import settings
from src.route.router import router
from config.endpoints_tags import tags_metadata
from logger.logger import logger, log_format, util_version
from set_response.response import error_response


_DisposableDomain = set()



app = FastAPI(openapi_tags=tags_metadata, title="nAI Configuration Management")


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc: HTTPException):
    return error_response(str(exc.detail), exc.status_code)


app.add_middleware(CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"])


if settings.PROFILING_ENABLED is True:
    add_timing_middleware(app, record=logger.info, prefix="app", exclude="untimed")


# print env vars
logger.info(f"env vars: {str(os.environ)}.")
logger.info(f"util_version: {util_version}.")


# Add route for APIs
app.include_router(router)


@app.get("/", tags=["System Endpoints"])
async def index():
    logger.info(log_format(msg='nAI configuration service is up.'))
    return "nAI configuration service is up."
