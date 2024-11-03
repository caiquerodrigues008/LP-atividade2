import math

# Função para verificar se os valores formam um triângulo
def forma_triangulo(a, b, c):
    return a < b + c and b < a + c and c < a + b

# Função para calcular a área do triângulo usando a fórmula de Herão
def area_triangulo(a, b, c):
    semi_perimetro = (a + b + c) / 2
    area = math.sqrt(semi_perimetro * (semi_perimetro - a) * (semi_perimetro - b) * (semi_perimetro - c))
    return area

# Entradas do usuário
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

# Verificação e cálculo da área
if forma_triangulo(a, b, c):
    area = area_triangulo(a, b, c)
    print(f"Os valores {a}, {b}, {c} formam um triângulo.")
    print(f"A área do triângulo é: {area:.2f}")
else:
    print(f"Os valores {a}, {b}, {c} não formam um triângulo.")
