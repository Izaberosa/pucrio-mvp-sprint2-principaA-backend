from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime, date
from typing import Union

from model import Base

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column("pk_usuario", Integer, primary_key=True)
    nome = Column(String(20))
    sobrenome = Column(String(50))
    cpf = Column(String(20))
    data_nascimento = Column(String(20))
    email = Column(String(50))
    joia = Column(String(10))



    def __init__(self, nome:str, sobrenome:str, cpf:str, data_nascimento:date, email:str, joia:str):
        """
        Cria um Usuario

        Arguments:
            
            nome: primeiro nome do usuario a ser criado.
            sobrenome: segundo nome do usuario.
            cpf: cpf do usuario.
            data_nascimento: data de nascimento do usuario.
            email: email para contato do usuario
            veiculo: nome do veiculo pertencente ao usuario
            placa: identificação do veículo
        """
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.email = email
        self.joia = joia