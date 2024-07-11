#ESCOPO GLOBAL

salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

salario_bonus(500) # 2500

print (salario_bonus(500)) #somou com o de cima 3000