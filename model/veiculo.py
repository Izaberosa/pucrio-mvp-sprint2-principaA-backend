from sqlalchemy import Column, String, Integer

from model import Base

class Veiculo(Base):
    __tablename__ = 'pedra'

    id = Column("pk_pedra", Integer, primary_key=True)
    nome_pedra = Column(String(20))
    modelo = Column(String(50))



    def __init__(self, nome_pedra:str, modelo:str):
        """
        Cria um veiculo

        Arguments:
            
            nome_veiculo: Nome do veiculo a ser cadastrado.
            modelo: Identificação do fabricante do veiculo.
            placa: Código de identificação de trânsito do veiculo.
           
        """
        self.nome_pedra = nome_pedra
        self.modelo = modelo
        
    