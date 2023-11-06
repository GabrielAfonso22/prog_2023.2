# Ac6 Gabriel Afonso e Marcus Vinícius 

# Exercício 1

from random import randint

dados=[]
cont=0
while cont < 100:
    num=randint (1,6)
    dados.append(num)
    cont+=1

print (dados)


print (dados.count(1))
print (dados.count(2))
print (dados.count(3))
print (dados.count(4))
print (dados.count(5))
print (dados.count(6))

# Exercício 2

import json

def adicionar_aluno(matricula, nome, email):
    alunos[matricula] = {"nome": nome, "e-mail": email}

alunos = {}

adicionar_aluno("6897", "Caio Madeira", " caio.m@gmail.com")
adicionar_aluno("2345", "Vinicius Marcus", "ViniMA@yahoo.com")
adicionar_aluno("8970", "Gabriel Silva", " GAsi@hotmail.com")

with open('alunos.json', 'w') as arquivo:
    json.dump(alunos, arquivo)

print("Dados dos alunos foram salvos em alunos.json")

# Exercício 3 

from datetime import datetime

def data_por_extenso(data_str):
    try:
        data = datetime.strptime(data_str, '%d/%m/%Y')
        mes_por_extenso = [
            'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
            'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
        ]
        dia = data.day
        mes = mes_por_extenso[data.month - 1]
        ano = data.year
        return f'{dia} de {mes} de {ano}'
    except ValueError:
        return None

data = '05/11/2023'
data_extenso = data_por_extenso(data)

if data_extenso is not None:
    print(data_extenso)
else:
    print('Data inválida')