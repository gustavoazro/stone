# teste de push
# importa Flask e request
from flask import Flask, request

# importa sqlite3
import sqlite3

# cria app Flask
app = Flask(__name__)

# cria conector com banco em memória e insere primeiros registros
conn = sqlite3.connect(':memory:', check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE cadastro (nome TEXT, sobrenome TEXT, cpf INTEGER, email TEXT, data_nasc VARCHAR)")
cursor.execute("INSERT INTO cadastro VALUES ('John', 'Travolta', 11122233344, 'john@travolta.com', '01/01/1950')")
cursor.execute("INSERT INTO cadastro VALUES ('Bob', 'Marley', 22233344455, 'bob@marley.com', '02/02/1950')")
conn.commit()


@app.route('/')
def home():
    return '''
              <h1>/consulta-todos</h1>
                  >Retorna todos os usuário cadastros (formato JSON)
              <h1>/consulta-cpf</h1>
                  >Retorna usuario utilizando CPF como parametro (formato JSON)
              <h1>/inserir</h1>
                  >Insere registro de usuario. Parametros em JSON (nome, sobrenome, cpf, email, data_nasc)'''


# rota de consulta para todos os registros
@app.route('/consulta-todos1', methods=['GET'])
def consulta_todos():
    # seleciona todos os usuarios da tabela
    rows = cursor.execute('SELECT * FROM cadastro').fetchall()
    return '''{}'''.format(rows)


# rota que consulta usuario por cpf
@app.route('/consulta-cpf', methods=['POST'])
def consulta_cpf():
    request_data = request.get_json()
    _cpf = request_data['cpf']
    rows = cursor.execute('SELECT * FROM cadastro WHERE cpf = ?', [_cpf]).fetchall()
    return '''{}'''.format(rows)


# rota para inserir um usuario
@app.route('/inserir', methods=['POST'])
def inserir():
    request_data = request.get_json()

    _nome = request_data['nome']
    _sobrenome = request_data['sobrenome']
    _cpf = request_data['cpf']
    _email = request_data['email']
    _data_nasc = request_data['data_nasc']
    dados = (_nome, _sobrenome, _cpf, _email, _data_nasc)
    cursor.execute("INSERT INTO cadastro (nome, sobrenome, cpf, email, data_nasc) VALUES (?,?,?,?,?)", dados)
    conn.commit()
    return '''Registro inserido!'''
