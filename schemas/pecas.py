from pydantic import BaseModel
from typing import Optional, List
from model.pecas import Peca


class PecaSchema(BaseModel):
    """ Define como uma nova peça deve ser inserido e representada
    """
    id: int = 1
    nome_peca: str = "Nome da joia"
    modelo_joia: str = "Identificação do tipo de joia"
    cod_joia: str = "Identificação da joia"



class ListagemPecaSchema(BaseModel):
    """ Define como uma listagem de peças será retornada.
    """
    materiais:List[PecaSchema]


class PecaBuscaPorIDSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no ID da mercadoria.
    """
    id: int = 1


def apresenta_materiais(materiais: List[Peca]):
    """ Retorna uma representação da peça seguindo o schema definido em
        ListagemPecaSchema.
    """
    result = []
    for peca in materiais:
        result.append({
            
            "nome_peca": peca.nome_peca,
            "modelo_joia": peca.modelo_joia,
            "cod_peca": peca.cod_joia,
        })

    return {"pecas": result}


class PecaViewSchema(BaseModel):
    """ Define como uma Peça será retornada: Peça.
    """
    id: int = 1
    nome_peca: str = "Nome da joia"
    modelo_joia: str = "Identificação do tipo de joia"
    cod_joia: str = "Identificação da joia"



class PecaDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    id: int



def apresenta_material(pecas: Peca):
    """ Retorna uma representação da Peça seguindo o schema definido em
        PeçaViewSchema.
    """
    return {
        "id": pecas.id,
        "nome_peca": pecas.nome_peca,
        "modelo_joia": pecas.modelo_joia,
        "cod_joia": pecas.cod_joia,
    }