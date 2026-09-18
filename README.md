# kipreco-python API

Projeto acadêmico desenvolvido durante as aulas de Programação Orientada a Objetos (POO). O objetivo principal é aplicar na prática os fundamentos da orientação a objetos, como herança, polimorfismo e encapsulamento, através da construção de uma API de ofertas.

## 🚀 O que a API faz até o momento
* **Módulo de Produtos:** Listagem, busca e filtragem de ofertas/produtos disponíveis (dados mockados).
* **Módulo de Autenticação (Login):** Validação de credenciais de usuários e retorno de permissões de acesso baseadas em perfis hierárquicos (Visitante, Contribuidor e Moderador) utilizando herança e polimorfismo.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3
* **Framework:** FastAPI
* **Servidor:** Uvicorn

## 📂 Estrutura do Repositório
A arquitetura do projeto segue o padrão MVC (Model-View-Controller) adaptado para APIs:

```text
kipreco-python/
├── app/
│   ├── controllers/   # Lógica de negócio e intermediação
│   ├── data/          # Dados mockados (ex: usuarios_mock.py)
│   ├── models/        # Classes base, entidades (herança/encapsulamento)
│   └── routes/        # Endpoints da API (produtos, auth)
├── venv/              # Ambiente virtual isolado
├── .gitignore         # Arquivos ignorados pelo Git
├── LICENSE            # Licença de uso do projeto
├── main.py            # Arquivo principal para inicialização da API
├── README.md          # Documentação do projeto
└── requirements.txt   # Dependências do projeto
```
## ⚙️ Como executar e testar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/MarcosVinicius909/kioferta-python
   cd kipreco-python
   ```

2. **Crie e ative o ambiente virtual:**
   * No Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   * No Linux/Mac:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Inicie o servidor local:**
   ```bash
   uvicorn main:app --reload
   ```

5. **Acesse a documentação interativa:**
   Abra o navegador e acesse o Swagger UI em:
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 📄 Licença
Este projeto está sob a licença definida no arquivo `LICENSE` presente na raiz do repositório.
