#1 exercício

def e_primo(num):
    primo = True

    for div in range(2, num):
        if num % div == 0:
            primo = False
            print(f"{num} não é primo. Divisível por {div}")

    if primo:
        print(f"{num} é primo")

e_primo(31) 
e_primo(32)

#2 exercício

def calcular_parcelas(divida):
    opcao_parcelamento = [1, 3, 6, 9, 12]
    tabela_juros = {1: 0, 3: 10, 6: 15, 9: 20, 12: 25}

    for parcelas in opcao_parcelamento:
        juros = tabela_juros[parcelas] / 100 * divida
        valor_total = divida + juros
        valor_parcela = valor_total / parcelas

        print(f"Opção de parcelamento em {parcelas} vezes: ")
        print(f"Valor dos juros: {juros}")
        print(f"Valor total da dívida: {valor_total}")
        print(f"Quantidade de parcelas: {parcelas}")
        print(f"Valor da parcela: {valor_parcela}")
        print("-" * 30)

divida = float(input("Digite o valor da dívida: "))
calcular_parcelas(divida)

#3 exercício

def cont_intervalos():
    intervalos = [0, 0, 0, 0]

    while True:
        num = int(input("Digite um número (ou um número negativo para sair): "))

        if num < 0:
            break

        if 0 <= num <= 25:
            intervalos[0] += 1
        elif 26 <= num <= 50:
            intervalos[1] += 1
        elif 51 <= num <= 75:
            intervalos[2] += 1
        elif 76 <= num <= 100:
            intervalos[3] += 1

    print(f"Números no intervalo [0-25]: {intervalos[0]}")
    print(f"Números no intervalo [26-50]: {intervalos[1]}")
    print(f"Números no intervalo [51-75]: {intervalos[2]}")
    print(f"Números no intervalo [76-100]: {intervalos[3]}")

cont_intervalos()

