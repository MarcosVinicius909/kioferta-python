from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.controllers.auth_controller import AuthController

router = APIRouter(prefix='/api/auth', tags=['auth'])
controller = AuthController()

class LoginRequest(BaseModel):
    nome: str
    senha: str

@router.post('/login')
def login(dados: LoginRequest):
    usuario_logado = controller.login(dados.nome, dados.senha)
    if not usuario_logado:
        raise HTTPException(status_code=401, detail='nome ou senha inválidos')
    return usuario_logado
