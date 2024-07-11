def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

calcular_total([10, 20, 34])  #64
retorna_antecessor_e_sucessor(10) # (9, 11)

print(calcular_total([10, 20, 34]))
print(retorna_antecessor_e_sucessor(10))
#retorna em tupla

