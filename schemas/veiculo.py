from typing import Any, List
from pydantic import BaseModel

from model.veiculo import Veiculo


class VeiculoSchema(BaseModel):
    """ Define como modelo padrao caso nao seja inserido um novo veículo.
    """
    id: int = 1
    nome_pedra: str = "Nome da Pedra"
    modelo: str = "Identificação do fabricante"


class UpdateVeiculoSchema(BaseModel):
    """ Define como um novo veículo pode ser atualizado.
    """
    id: int = 1
    nome_pedra: str = "Nome da Pedra"
    modelo: str = "Identificação do fabricante"



class VeiculoBuscaSchema(BaseModel):
    """ Define como a estrutura de pesquisa(busca) deve ser representada. Que será
        feita apenas com base no nome do veículo.
    """
    nome_pedra: str = "Digite o nome do veículo"


class VeiculoBuscaPorIDSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no ID do veículo.
    """
    id: int = 1


class ListagemVeiculoSchema(BaseModel):
    """ Define como uma listagem de veículo será retornada.
    """
    nomes:List[VeiculoSchema]


def apresenta_veiculos(nomes: List[Veiculo]):
    """ Retorna uma representação do veículo seguindo o schema definido em
        VeiculoSchema.
    """
    result = []
    for pedra in nomes:   
        result.append({
            
            "nome_pedra": pedra.nome_pedra,
            "modelo": pedra.modelo,
        })

    return {"veiculos": result}


class VeiculoViewSchema(BaseModel):
    """ Define um modelo de como o veículo será representado.
    """

    id: int = 1
    nome_pedra: str = "Nome da Pedra"
    modelo: str = "Identificação do fabricante"
    


class VeiculoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    id: int

def apresenta_veiculo(veiculo: Veiculo):
    """ Retorna uma representação do veículo seguindo o schema definido em
        VeiculoViewSchema.
    """

    return {
        "id": veiculo.id,
        "nome_pedra": veiculo.nome_pedra,
        "modelo": veiculo.modelo,
    }
