# Exercício 1

def imprimir_dados(n, i=1):
    if i > n:
        return
    for x in range(1, i + 1):
        print(x, end="   ")
    print()
    imprimir_dados(n, i + 1)

n = int(input("Digite um número inteiro: "))
imprimir_dados(n)

# Exercício 2

def conta_digitos(numero):
    return len(str(numero))

numero = int(input("Digite um número inteiro: "))
quant_digitos = conta_digitos(numero)
print(f"O número {numero} possui {quant_digitos} dígitos.")

# Exercício 3

try:
    num1 = int(input("Informe um número inteiro: "))
    num2 = int(input("Informe o segundo número inteiro: "))
    
    resultado = num1 / num2

except ValueError:
    print("Digite somente números inteiros(ERRO).")
except ZeroDivisionError:
    print("Não é possível dividir por zero(ERRO).")
finally:
    try:
        print(f"O resultado é: {resultado}")
    except NameError:
        print("Não foi possível concluir a operação devido a erros anteriores.")

