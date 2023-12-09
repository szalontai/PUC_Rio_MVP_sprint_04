from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

# colunas = Weight,Height,Age,Outcome

class Cliente(Base):
    __tablename__ = 'clientes'
    
    id = Column(Integer, primary_key=True)
    name= Column("Name", String(50))
    weight = Column("Weight", Float)
    height = Column("Height", Float)
    age = Column("Age", Float)
    outcome = Column("Size", String(10), nullable=True)
    data_insercao = Column(DateTime, default=datetime.now())
    
    def __init__(self, name:str,weight:float, 
                 age:float, height:float, outcome:str, 
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Cliente

        Arguments:
        name: nome do cliente
            weight: peso
            height: altura
            age: idade
            outcome: diagnóstico, tamanho
            data_insercao: data de quando o cliente foi inserido à base
        """
        self.name=name
        self.weight = weight
        self.height = height
        self.age = age
        self.outcome = outcome

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao