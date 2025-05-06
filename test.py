import requests


def filtro(dados):
    r = requests.post('http://localhost:5000/filtro', json=dados)
    print(r.text)

def limit(n):
    r = requests.get(f'http://localhost:5000/limit/{n}')
    print(r.text)

def attack_type(attack_type):
    r = requests.get(f'http://localhost:5000/attack_type/{attack_type}')
    print(r.text)

def insert(dados):
    r = requests.post('http://localhost:5000/insere', json=dados)
    print(r.text)

def update(id, dados):
    r = requests.post(f'http://localhost:5000/update/{id}', json=dados)
    print(r.text)

def delete(id):
    r = requests.post(f'http://localhost:5000/delete/{id}')
    print(r.text)

dados_filtro = {
    "Attack Type": "DDoS",
    "Target Industry": "Government",
}

print("Testando o filtro")
filtro(dados_filtro)

print("Testando o limit")
limit(5)

print("Testando o attack_type")
attack_type("DDoS")

print("Testando o insert")
dados_insert = {
    "Attack Type": "DDoS",
    "Target Industry": "Government",
    "Country": "Brazil",
    "Year": 2025,
    "Financial Loss (in Million $)": 10000,
    "Number of Affected Users": 5000,
    "Attack Source": "Unknown",
    "Security Vulnerability Type": "Zero-day",
    "Defense Mechanism": "Firewall",
    "Incident Resolution Time (in Hours)": 24,
}
insert(dados_insert)

print("Testando o update")
dados_update = {
    "Attack Type": "DDoS",
    "Target Industry": "Government",
    "Country": "Brazil",
    "Year": 2025,
    "Financial Loss (in Million $)": 20000,
    "Number of Affected Users": 10000,
    "Attack Source": "Unknown",
    "Security Vulnerability Type": "Zero-day",
    "Defense Mechanism": "Firewall",
    "Incident Resolution Time (in Hours)": 12,
}
update(0, dados_update)

print("Testando o delete")
delete(0)