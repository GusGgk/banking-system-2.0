def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def test(a, b):
    return a * 2 + b * 3

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")

exibir_resultado(10, 10, somar) # O resultado da operação 10 + 10 = 20
exibir_resultado(10, 10, subtrair) # O resultado da operação 10 - 10 = 0
exibir_resultado(10, 10, test)  # O resultado da operação é = 50