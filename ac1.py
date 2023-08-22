
#algoritimo para calcular equações do 2 grau.

coeficienteA = float(input("Digite o valor de A : "))

coeficienteB = float(input("Digite o valor de  B : "))

coeficienteC = float(input("Digite o valor de C : "))

delta = coeficienteB ** 2-4 * coeficienteA * coeficienteC

raizdedelta = delta ** 0.5

x1 = (- coeficienteB + raizdedelta) / (2 * coeficienteA)

x2 = (- coeficienteB - raizdedelta) / (2 * coeficienteA)

print(" Delta:{}\n Raiz de Delta:{}\n X1:{}\n X2:{}".format(delta, raizdedelta, x1, x2))

# Elaborar um programa que leia uma variável inteira ano.

ano = int(input("digite o ano: "))

bissexto = ano % 4 == 0 and \
(ano % 100 != 0 or ano % 400 == 0)

print("É bissexto: ", bissexto)
