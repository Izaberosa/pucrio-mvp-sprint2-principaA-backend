from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os
import psycopg2

# importando os arquivos criados na pasta model
from model.base import Base
from model.usuario import Usuario
from model.veiculo import Veiculo
from model.pecas import Peca

db_path = "database/"
# Verifica se o diretorio não existe
if not os.path.exists(db_path):
   # então cria o diretorio
   os.makedirs(db_path)


# cria a engine de conexão com o banco
# engine = create_engine("postgresql://postgres:Rcost30anubi@localhost:5432/postgres", echo = True)
db_url = 'sqlite:///%s/db.sqlite3' % db_path

# cria a engine de conexão com o banco
engine = create_engine(db_url, echo=False)

# Instancia um criador de seção com o banco
Session = sessionmaker(bind=engine)

# cria o banco se ele não existir 
if not database_exists(engine.url):
    create_database(engine.url) 

# cria as tabelas do banco, caso não existam
Base.metadata.create_all(bind=engine)
