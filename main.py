'''
uvicorn main:app --reload  
http://127.0.0.1:8000
'''

from fastapi import FastAPI

app = FastAPI()

from controller.auth_router import auth_router
from controller.categoria_router import categoria_router 
from controller.transacao_router import transacao_router
from controller.usuario_router import usuario_router

app.include_router(usuario_router)
app.include_router(auth_router)
app.include_router(categoria_router)
app.include_router(transacao_router)

