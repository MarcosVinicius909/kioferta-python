from app.models.usuario import carregar_usuarios

class AuthController:
    def __init__(self):
        self._usuarios = carregar_usuarios()

    def login(self, nome, senha):
        for u in self._usuarios:
            if u.mostrar_nome() == nome and u.conferir_senha(senha):
                return self._para_dicionario(u)
        return None

    def _para_dicionario(self, usuario):
        return {
            "id": usuario.mostrar_id(),
            "nome": usuario.mostrar_nome(),
            "perfil": usuario.mostrar_perfil(),
            "permissoes": {
                "favoritar": usuario.pode_favoritar(),
                "publicar": usuario.pode_publicar(),
                "moderar": usuario.pode_moderar()
            }
        }