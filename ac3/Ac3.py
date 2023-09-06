# 1 Exercício

def reajuste_salarial(salario_atual):
    if salario_atual <= 280:
        aumento_percentual = 20
    elif salario_atual <= 700:
        aumento_percentual = 15
    elif salario_atual <=1500:
        aumento_percentual = 10
    else:
        aumento_percentual = 5

    aumento = (salario_atual * aumento_percentual)/100
    novo_salario = salario_atual + aumento

    return aumento_percentual, aumento, novo_salario 

salario_atual= float(input("Digite o salário atual do funcionário:R$ "))

percentual,aumento,novo_salario = reajuste_salarial(salario_atual)

print(f"Salário antes do reajuste: R$ {salario_atual:.2f}")
print(f"Percentual de aumento aplicado: {percentual}%")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário após o aumento: R$ {novo_salario:.2f}")

#2 Exercício

def dia_da_semana(num):
    if num == 1:
        return "Domingo"
    elif num == 2:
        return "Segunda-Feira" 
    elif num == 3:
        return "Terça-Feira" 
    elif num == 4:
        return "Quarta-Feira"
    elif num == 5:
        return "Quinta-Feira" 
    elif num == 6:
        return "Sexta-Feira" 
    elif num == 7:
        return "Sábado" 
    else:
        return "valor inválido"
    
print (dia_da_semana(1))

#3 Exercício

def calcular_raizes(a, b, c):
    resultado = ""

    if a == 0:
        resultado = "A equação não é do segundo grau. Encerrando o programa."
    else:
        delta = b ** 2 - 4 * a * c

        if delta < 0:
            resultado = "A equação não possui raízes reais. Encerrando o programa."
        elif delta == 0:
            raiz = -b / (2 * a)
            resultado = f"A equação possui uma raiz real: x = {raiz}"
        else:
            raiz1 = (-b + (delta ** 0.5)) / (2 * a)
            raiz2 = (-b - (delta ** 0.5)) / (2 * a)
            resultado = f"A equação possui duas raízes reais:\nx1 = {raiz1}\nx2 = {raiz2}"

    return resultado

a = float(input("Digite o valor de a: "))

if a == 0:
    resultado = "A equação não é do segundo grau. Encerrando o programa."
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    resultado = calcular_raizes(a, b, c)

print(resultado)



    

