from sqlalchemy import Column, String, Integer, DateTime
from typing import Union

from  model import Base


class Peca(Base):

    __tablename__ = 'joias'

    id = Column("pk_cod_joias", Integer, primary_key=True)
    nome_joias = Column(String(50))
    modelo_joia = Column(String(20))
    cod_joia = Column(String(20))
    
    

    def __init__(self, nome_joias:str, modelo_joia:str, cod_joia:str,
                data_insercao:Union[DateTime, None] = None):
        """
        Cria um Produto

        Arguments:
            nome: nome do produto.
            preco: preço atual do produto
            descricao: descrição do produto fornecida pelo fabricante
            marca: identicação da fabricante
            categoria: categoria atribuída ao produto pela loja
            data_insercao: data de quando o produto foi inserido à base
        """
        self.nome_joias = nome_joias
        self.modelo_joia = modelo_joia
        self.cod_joia = cod_joia
        

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao