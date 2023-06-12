from fastapi import FastAPI
from routers.vehiculo import vehiculo
from config.database import engine, Base

app = FastAPI()
app.include_router(vehiculo)
Base.metadata.create_all(bind=engine)