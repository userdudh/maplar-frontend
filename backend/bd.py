from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
import os

BACKEND_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BACKEND_DIR)

db_folder = os.path.join(ROOT_DIR, "database")
db_path = os.path.join(db_folder, "maplar.db")

os.makedirs(db_folder, exist_ok=True)

db = create_engine(f'sqlite:///{db_path}')
# db = create_engine('sqlite:///../database/maplar.db')
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    sobrenome = Column("sobrenome", String)
    email = Column("email", String)
    telefone = Column("telefone", String)
    senha = Column("senha", String)

    # def __init__(self, nome, sobrenome, email, telefone, senha):
    #     self.nome = nome
    #     self.sobrenome = sobrenome
    #     self.email = email
    #     self.telefone = telefone
    #     self.senha = senha

class Imovel(Base):
    __tablename__ = "imoveis"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    proprietario = Column("proprietario", ForeignKey("usuarios.id"))
    titulo = Column("titulo", String)
    valor = Column("valor", Float)
    imagem = Column("imagem", String) #nao sei
    tipo = Column("tipo", String)
    tamanho = Column("tamanho", Float)
    quarto = Column("quarto", Integer)
    banheiro = Column("banheiro", Integer)
    garagem = Column("garagem", Integer)
    descricao = Column("descricao", String)
    cep = Column("cep", String)
    bairro = Column("bairro", String)
    rua = Column("rua", String)
    numero = Column("numero", String)

    # def __init__(self, proprietario, titulo, valor, imagem, tipo, tamanho, quarto, banheiro, garagem, descricao, cep, bairro, rua, numero):
    #     self.proprietario = proprietario
    #     self.titulo = titulo
    #     self.valor = valor
    #     self.imagem = imagem
    #     self.tipo = tipo
    #     self.tamanho = tamanho
    #     self.quarto = quarto
    #     self.banheiro = banheiro
    #     self.garagem = garagem
    #     self.descricao = descricao
    #     self.cep = cep
    #     self.bairro = bairro
    #     self.rua = rua
    #     self.numero = numero

Base.metadata.create_all(bind=db)
