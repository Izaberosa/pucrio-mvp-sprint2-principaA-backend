from typing import Any, List
from pydantic import BaseModel, validator, root_validator, Field
from datetime import date

from sqlalchemy import values
from model.usuario import Usuario
import re


class UsuarioSchema(BaseModel):
    """ Define como modelo padrao caso nao seja inserido um novo usuario.
    """
    nome: str = "Izabelle"
    sobrenome:  str = "Rosa de Oliveira"
    cpf: str = "373.031.238-30"
    data_nascimento: str = "11/02/2001"
    email: str = "izabellerosa0@gmail.com"
    joia: str = "identificacao da joia"


    """ Verifica e restringe o cpf no formato especificado (000.000.000-00)
    """
    @validator('cpf')
    def valida_cpf(cls, v):
        if re.search("^\d{3}\x2E\d{3}\x2E\d{3}\x2D\d{2}$", v):
            return v

        raise ValueError('O CPF informado nao condiz com o formato padrao 000.000.000-00')
    
        
    """ Permita apenas a data no formato especificado (dd/mm/aaaa)
    """
    @validator('data_nascimento')
    def valida_data_nascimento(cls, v):
        if re.search("[0-9]{2}\/[0-9]{2}\/[0-9]{4}", v):
            return v

        raise ValueError('A data tem que ser no formato dd/mm/aaaa')
    
        
    """ Verifica e restringe o email no formato especificado (nome@email.com)
    """
    @validator('email')
    def valida_email(cls, v):
        if re.search("[a-zA-Z0-9]+@[a-zA-Z0-9]+\.com[\.a-zA-Z]{0,3}", v):
            return v

        raise ValueError('O email tem que ter o formato nome@email.com')


class UsuarioBuscaSchema(BaseModel):
    """ Define a estrutura de pesquisa(busca) deve ser representada. Que será
        feita apenas com base no nome do usuario.
    """
    nome: str = "Digite o nome do usuario"


class ListagemUsuariosSchema(BaseModel):
    """ Define como uma listagem de usuarios será retornada.
    """
    nomes:List[UsuarioSchema]


def apresenta_usuarios(nomes: List[Usuario]):
    """ Retorna uma representação do usuario seguindo o schema definido em
        UsuarioSchema.
    """
    result = []
    for usuario in nomes:   
        result.append({
            
            "nome": usuario.nome,
            "sobrenome": usuario.sobrenome,
            "cpf": usuario.cpf,
            "data_nascimento": usuario.data_nascimento,
            "email": usuario.email,
            "joia": usuario.joia,
            
        })

    return {"usuarios": result}


class UsuarioViewSchema(BaseModel):
    """ Define um modelo de como o usuario sera representado.
    """

    id: int = 1
    nome: str = "Izabelle Rosa"
    sobrenome:  str = "de Oliveira"
    cpf: str = "373.031.238-30"
    data_nascimento: str = "11/02/2001"
    email: str = "izabellerosa0@gmail.com"
    joia: str = "identificacao da joia"
    


class UsuarioDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_usuario(usuario: Usuario):
    """ Retorna uma representação do usuario seguindo o schema definido em
        UsuarioViewSchema.
    """
    return {
        "nome": usuario.nome,
        "sobrenome": usuario.sobrenome,
        "cpf": usuario.cpf,
        "data_nascimento": usuario.data_nascimento,
        "email": usuario.email,
        "joia": usuario.joia,
    }
