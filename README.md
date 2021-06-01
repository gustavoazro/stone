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

**Pipeline - CI**
  - Ferramenta: GitHub Actions (Build app.py dentro do container e publica no Docker Hub)
  - Arquivo: stone/.github/workflows/ci_docker_hub.yml
  - Destino do container (Docker Hub): gustavoazro/stone:latest

**Publicação do app no GKE (conforme tabela acima)**
  - http://35.232.33.46/ (Índice)
  - http://35.232.33.46/consulta-todos
  - http://35.232.33.46/consulta-cpf
  - http://35.232.33.46/inserir
