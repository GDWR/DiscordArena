import os

import uvicorn
from fastapi import FastAPI
from fastapi_pagination import add_pagination

from database import create_all_tables
from database import database as db
from routes import develop_router, item_router, player_router

app = FastAPI()

if os.getenv("ENVIRONMENT") is None:
    app.include_router(develop_router)

app.include_router(player_router)
app.include_router(item_router)


@app.on_event("startup")
async def _on_startup():
    await db.connect()
    create_all_tables()


@app.on_event("shutdown")
async def _on_shutdown():
    await db.disconnect()

add_pagination(app)
uvicorn.run(app, host="0.0.0.0", port=80)
