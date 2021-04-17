import uvicorn
from fastapi import FastAPI

from .routes import player_router
from .database import create_all_tables
from .database.db import database as db

app = FastAPI()

app.include_router(player_router)

@app.on_event("startup")
async def start_up():
    await db.connect()
    create_all_tables()


@app.on_event("shutdown")
async def shutdown_event():
    await db.disconnect()


uvicorn.run(app, host="0.0.0.0", port=80)
