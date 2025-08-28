class produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

leite = produto('leite', 7.99, 10)

print(leite.nome)
