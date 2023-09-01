# Trabalho Ac2

# 1 Exercício

salario_hora = float(input('Digite seu salário por hora: '))

horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))

salario_receber = salario_hora*horas_trabalhadas

print('Você ira receber $: ',salario_receber)

# 2 exercício

n1 = int(input("Digite o primeiro numero:  "))
n2 = int(input("Digite o segundo numero:  "))
nReal = float(input("Digite o numero Real:  "))

r1 = n1 * 2 * (n2 / 2) 
r2 = n1 *  3 + nReal
r3 = nReal ** 3

print ("o produto do dobro do primeiro com metade do segundo = ",r1), 
print ("a soma do triplo do primeiro com o terceiro = ", r2), 
print ("o terceiro elevado ao cubo = ", r3)

# 3 exercício

def resultado(n1, n2, n3):
    resultado1 = (2 * n1) * (0.5 * n2)
    resultado2 = (3 * n1) + n3
    resultado3 = n3 ** 3

    return resultado1, resultado2, resultado3

n1 = 25
n2 = 15
n3 = 9

resultado1, resultado2, resultado3 = resultado(n1, n2, n3)

print(f"O produto do dobro do primeiro com metade do segundo é: {resultado1}")
print(f"A soma do triplo do primeiro com o terceiro é: {resultado2}")
print(f"O terceiro elevado ao cubo é: {resultado3}")


# 4 exercício

ano = int(input("ano: "))

bissexto = ano % 4 == 0 and \
(ano % 100 != 0 or ano % 400 ==0)

print ("é bissexto: " , bissexto)