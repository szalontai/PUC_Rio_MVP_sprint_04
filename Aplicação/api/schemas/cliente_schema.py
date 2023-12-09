from pydantic import BaseModel
from typing import Optional, List
from model.cliente import Cliente
import json
import numpy as np

class ClienteSchema(BaseModel):
    """ Define como um novo cliente a ser inserido deve ser representado
    """
    name: str = "Maria"
    weight: float = 60.0
    height: float = 148.0
    age: int = 50
    
class ClienteViewSchema(BaseModel):
    """Define como um cliente será retornado
    """
    id: int = 1
    name: str = "Maria"
    weight: float = 60.0
    height: float = 148.0
    age: int = 50
    outcome: str = None
    
class ClienteBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no nome do cliente.
    """
    name: str = "Maria"

class ListaClientesSchema(BaseModel):
    """Define como uma lista de clientes será representada
    """
    clientes: List[ClienteSchema]

    
class ClienteDelSchema(BaseModel):
    """Define como um cliente para deleção será representado
    """
    name: str = "Maria"
    
# Apresenta apenas os dados de um cliente    
def apresenta_cliente(cliente: Cliente):
    """ Retorna uma representação do cliente seguindo o schema definido em
        ClienteViewSchema.
    """
    return {
        "id": cliente.id,
        "name": cliente.name,
        "weight": cliente.weight,
        "height": cliente.height,
        "age": cliente.age,
        "outcome": cliente.outcome
    }
    
# Apresenta uma lista de clientes
def apresenta_clientes(clientes: List[Cliente]):
    """ Retorna uma representação do cliente seguindo o schema definido em
        ClienteViewSchema.
    """
    result = []
    for cliente in clientes:
        result.append({
            "id": cliente.id,
            "name": cliente.name,
            "weight": cliente.weight,
            "height": cliente.height,
            "age": cliente.age,
            "outcome": cliente.outcome
        })

    return {"clientes": result}
