from models.vehiculo import Vehiculo as VahiculoModel
from schemas.vehiculo import Vehiculo

class VehiculoService():
    def __init__(self, db) -> None:
        self.db = db
    
    def create_vehiculo(self, vehiculo: Vehiculo):
        new_vehiculo = VahiculoModel(**vehiculo.dict())
        self.db.add(new_vehiculo)
        self.db.commit()