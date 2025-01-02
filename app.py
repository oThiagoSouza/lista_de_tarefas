from flask import Flask, render_template, redirect, request
import pyodbc as db

dados_conexao = ("Driver={ODBC Driver 18 for SQL Server};"
                "Server=tcp:thiago.database.windows.net,1433;"
                "Database=controle_gastos;"
                "Uid=CloudSAc620f1c0;"
                "Pwd={Au12062107};"
                "Encrypt=yes;"
                "TrustServerCertificate=no;")


conexao = db.connect(dados_conexao)
cursor = conexao.cursor()


app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    cursor.execute(f"SELECT * FROM tasks")
    tasks = cursor.fetchall()
    task = request.form['nome']
    nome_pessoa = request.form['pessoa']
    data_limite = request.form['data']
    descricao = request.form['desc']
    acao = request.form.get('acao')

    if acao == 'cadastrar' and task == '':
        return redirect('/')
    elif acao == 'cadastrar' and task == ' ':
        return redirect('/')
    elif acao == 'cadastrar':
        cursor.execute(f"INSERT INTO tasks(nome, dt_limite, descricao, pessoa) VALUES('{task}', '{data_limite}', '{descricao}', '{nome_pessoa}')")
        cursor.commit()
        return redirect('/')
    elif acao == 'visualizar':
        return render_template("index.html", tasks=tasks)
    elif acao == 'deletar':
        cursor.execute("DELETE FROM tasks")
        cursor.commit()
        return redirect('/')

if __name__ == "__main__":
    app.run()