from datetime import datetime
from config.database import Base
from sqlalchemy import Column, Integer, String, DateTime

class Vehiculo (Base):
    __tablename__= "vehiculo"
    id = Column (Integer, primary_key=True)
    placa = Column (String(10),nullable=False,unique=True)


    '''
    Crea la fecha actual cuando se crea el registro
    fecha = Column(DateTime(),default=datetime.now())
    '''