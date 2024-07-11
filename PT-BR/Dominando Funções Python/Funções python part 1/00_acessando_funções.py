#def serve para informar que o nome da função é _____
def exibir_mensagem():
    print("Olá mundo")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome= "Anônimo"):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem()
exibir_mensagem_2("Gustavo")
exibir_mensagem_3()
exibir_mensagem_3(nome="Malu")