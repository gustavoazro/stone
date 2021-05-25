from sqlite3.dbapi2 import Connection
from flask import Flask, request, render_template
app = Flask(__name__)

import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

cursor.execute("CREATE TABLE user (name TEXT, password TEXT, cpf INTEGER)")
cursor.execute("INSERT INTO user VALUES ('Sammy', 'shark', 1)")
rows = cursor.execute("SELECT name, password, cpf FROM user").fetchall()

print(__name__)

@app.route('/user/<name>')
def hello(name=None):
  #name=None ensures the code runs even when no name is provided
  return render_template('user-profile.html', name=name)