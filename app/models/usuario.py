from app.data.usuarios_mock import USUARIOS

class Usuario:
    def __init__(self, id, nome, senha):
        self._id = id
        self._nome = nome
        self._senha = senha

    def mostrar_id(self):
        return self._id

    def mostrar_nome(self):
        return self._nome

    def conferir_senha(self, senha):
        return self._senha == senha

    def mostrar_perfil(self):
        return type(self).__name__

    def pode_favoritar(self):
        return True

    def pode_publicar(self):
        return False

    def pode_moderar(self):
        return False


class Visitante(Usuario):
    pass


class Contribuidor(Usuario):
    def pode_publicar(self):
        return True


class Moderador(Contribuidor):
    def pode_moderar(self):
        return True


def carregar_usuarios():
    PERFIS = {
        'visitante': Visitante,
        'contribuidor': Contribuidor,
        'moderador': Moderador
    }
    return [PERFIS[u['perfil']](u['id'], u['nome'], u['senha']) for u in USUARIOS]