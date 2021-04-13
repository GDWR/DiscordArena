import uvicorn
from fastapi import FastAPI

from routes import player_router
from database import create_all_tables, engine

app = FastAPI()


app.include_router(player_router)


@app.on_event("startup")
async def _start_up():
    engine.connect()
    await create_all_tables()



@app.on_event("shutdown")
async def _shutdown_event():
    await engine.disconnect()


uvicorn.run(app, host="0.0.0.0", port=80)
