def dividir(dividendo, divisor):
    print(divisor.resultado)
    return dividendo / divisor

def testa_divisão(divisor):
    try:
        resultado = dividir(10, divisor)
        print(f"O resultado da divisão de 10 por {divisor} é {resultado}")
    except:
        print("Erro por divisao por zero tratado")

try:
    testa_divisão(0)
except AttributeError:
    print("Erro de atributo")


print("Programa encerrado")