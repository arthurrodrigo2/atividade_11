'''
Crie um programa que receba do usuário os valores "a" e "b" e envie para uma função que calcule a função do 1º grau. Ao final, o programa mostre o valor de "x".
'''

# função para calcular o valor de "x"
def calcular_x(a, b):
    if a == 0:
        raise ValueError("O valor de 'a' não pode ser igual a zero.")
    x = -b / a
    return x

# programa
print("CALCULAR O VALOR DE  NA FUNÇÃO DO 1º GRAU")

# usuário informa os valores de a e b
a = float(input("Informe o valor de 'a': ").replace(",", "."))
b = float(input("Informe o valor de 'b': ").replace(",", "."))

# exibe na tela o valor de x
try:
    print(f"O valor de x é {calcular_x(a, b):.2f}.")
except ValueError as e:
    print(f"Erro: {e}")

