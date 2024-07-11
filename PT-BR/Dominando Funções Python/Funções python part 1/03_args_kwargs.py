def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema(
    #data_extenso
    "Quinta-Feira, 10 de Julho de 2024",
     #*args
     "Zen of Python",
     "Beautiful is better than ugly.",
     #** kwargs
     autor = "Tim Peters",
     ano=1999
)
