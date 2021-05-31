# DESAFIO > Stone DevOps | SRE

Repositório elaborado e construído para cumprir o desafio SRE/DevOps:
> https://github.com/stone-payments/stone-sre-devops-challenge

Repositório de resposta ao desafio: 
> https://github.com/gustavoazro/stone

## Entregável 1

**API: Linguagem de desenvolvimento (Python/Flask)**
  - Arquivo: /app.py
  - Banco de dados: sqlite com persistência em memória
  - Estrutura do App
  
  Local | Ação
  ------|------
  '/' | Acessa índice com as opções
  /consulta-todos | Retorna todos os registros em JSON (GET)
  /consulta-cpf | Retorna registro em JSON (POST)
  /inserir | Insere registro em JSON (POST)

**Container**
  - Arquivo: Dockerfile, requirements.txt

**Pipeline**
  - Ferramenta: GitHub Actions
