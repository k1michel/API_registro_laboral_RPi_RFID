from typing import Optional 
from fastapi import FastAPI
from pydantic import BaseModel 
from datetime import datetime

import uvicorn
from gestor_base_datos import Conexion


class api(BaseModel):
    nombre: str
    ano: int 
    mes: int
    dia: int
    hora: str
    tipo: str


proyecto_registro_laboral = FastAPI()

bdd = Conexion()



if __name__ == "__main__":
    uvicorn.run(proyecto_registro_laboral, host="0.0.0.0", port=8080)