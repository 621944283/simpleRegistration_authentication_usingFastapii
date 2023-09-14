from fastapi import FastAPI

from fastapi import FastAPI


from models import Base
from database import engine
from fastapi.staticfiles import StaticFiles
from routers import register,login,profile

from starlette.middleware.sessions import SessionMiddleware


Base.metadata.create_all(bind=engine)
tags_metadata = [

    {
        'name':'Admin/Dashboard ',
        'description':'Api Admin to control all function in this app'
    },
]

app = FastAPI(
        title='Simple test',
        description='simple test',
        docs_url='/docs',
        openapi_tags=tags_metadata
        # openapi_prefix=None
    )
app.include_router(register.router)
app.include_router(login.router)
app.include_router(profile.router)