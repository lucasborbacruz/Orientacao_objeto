class Escola:
    # Start da Classe POO
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nota1 = None
        self.nota2 = None
        self.nota_final = None

    def apresentar(self):
        print(f"""
                O aluno {self.nome}
              """)
    
    def nota(self, nota_1, nota_2):
        self.nota1 = nota_1
        self.nota2 = nota_2
    
    def calcula(self):
        self.nota_final = (self.nota1+self.nota2)/2
        if self.nota_final >= 7:
            print(f"{self.nome} aprovado {self.nota_final}")
        elif self.nota_final >= 4 and self.nota_final < 7:
            print(f"{self.nome} recuperação {self.nota_final}")
        else:
            print(f"{self.nome} reprovado {self.nota_final}")


