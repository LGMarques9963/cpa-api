from flask import Flask, request
import pandas as pd

app = Flask(__name__)
db_name = 'global-cybersecurity-threats-2015-2024/Global_Cybersecurity_Threats_2015-2024.csv'

db = pd.read_csv(db_name)

@app.route("/insere", methods=['POST'])
def insert():
    global db
    db = pd.read_csv(db_name)
    dados = request.get_json()
    if dados:
        # Adiciona os dados recebidos ao DataFrame
        db = db._append(dados, ignore_index=True)
        # Salva o DataFrame atualizado no CSV
        db.to_csv(db_name, index=False)
        return f"Dados inseridos com sucesso: {dados}, id {db[db.columns[0]].max()}"
    else:
        return "Nenhum dado recebido."

@app.route("/attack_type/<string:attack_type>", methods = ['POST', 'GET'])
def attack_type(attack_type):
    global db
    db = pd.read_csv(db_name)
    return db[db['Attack Type'] == attack_type].to_json(orient='records')

@app.route("/limit/<int:n>", methods = ['POST', 'GET'])
def limit(n):
    global db
    db = pd.read_csv(db_name)
    return db.head(n).to_json(orient='records')

@app.route("/filtro", methods = ['POST', 'GET'])
def filter():
    global db
    db = pd.read_csv(db_name)
    filtro = request.get_json()
    if filtro:
        # Filtra os dados do DataFrame
        for key, value in filtro.items():
            db = db[db[key] == value]
        return db.to_json(orient='records')
    else:
        return "Nenhum filtro recebido."


@app.route("/update/<int:id>", methods = ['POST'])
def update(id):
    global db
    db = pd.read_csv(db_name)
    dados = request.get_json()
    if dados:
        # Atualiza os dados no DataFrame
        db.loc[id] = dados
        # Salva o DataFrame atualizado no CSV
        db.to_csv(db_name, index=False)
        return f"Dados atualizados com sucesso: {dados}, id {id}"
    else:
        return "Nenhum dado recebido."

@app.route("/delete/<int:id>", methods = ['POST'])
def delete(id):
    global db
    db = pd.read_csv(db_name)
    # Remove o dado do DataFrame
    db = db.drop(index=id)
    # Salva o DataFrame atualizado no CSV
    db.to_csv(db_name, index=False)
    return f"Dado com id {id} removido com sucesso."


if __name__ == "__main__":
    app.run(debug=True)