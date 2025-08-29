class Produto:
    def __init__(self, nome, preco, quantidade):
        # Atributos

        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

# Apresentacao
    def apresentacao(self):
        
        print(f"""
              produto : Nome: {self.nome} | Preço: {self.preco} | Quantidade: {self.quantidade}
        """)

leite = Produto('leite', 7.99, 10)
maca = Produto('maca', 0.99, 15)
agua = Produto('agua', 1.99, 20)

