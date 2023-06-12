from fastapi import APIRouter
from schemas.vehiculo import Vehiculo
from config.database import Session
from services.vahiculo import VehiculoService

vehiculo = APIRouter()

@vehiculo.post('/Crear',tags=['Vehiculo'])
def crear_vehiculo(vehiculo: Vehiculo):
    db = Session()
    VehiculoService(db).create_vehiculo(vehiculo)