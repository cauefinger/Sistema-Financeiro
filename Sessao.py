from database import engine
from sqlalchemy.orm import sessionmaker

def pegar_sessao():

    try:
        Sessao = sessionmaker(bind=engine)
        sessao = Sessao()
        yield sessao

    finally:
        sessao.close()