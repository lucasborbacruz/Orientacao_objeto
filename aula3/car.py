# Defini a classe chave
class Chave:
    # método construtor
    def __init__(self, marca):
        self.marca = marca
        self.ativa = False

# Defini a classe


class Car:
    def __init__(self, modelo, ano, cor, potencia, placa, chave: Chave):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.potencia = potencia
        self.placa = placa
        self.ligado = False
        self.aberto = False
        self.chave = chave
        self.velocidade = 0

        # método | Ação realizada pela classe
    def abrir_carro(self, chave):
        if not self.ligado and not self.aberto and self.chave.marca == chave.marca:
            self.ligado = True
            print("O carro está aberto!")

        else:
            print(" O carro já está aberto ou a chave é inválida!")

    def ligar_carro(self):
        if not self.ligado and self.aberto:
            self.ligado = True
            print("O carro está ligado!")

        else:
            print("O carro já está ligado ou está fechado!")

    def acelerar_carro(self):
        if self.ligado and self.velocidade >= 0:
            self.velocidade += 5
            print(f"O carro {self.modelo} velocidade {self.velocidade} km/h")

        else:
            print(f"O carro {self.modelo} está desligado ou parado!")

   # O carro tem que desligar, mas não pode desligar acelerado
    def desligar_carro(self):
        if self.ligado and self.velocidade == 0:
            self.ligado = False
            print(f"O carro {self.modelo} está desligado!")
        else:
            print(
                f"O carro {self.modelo} está ligado ou em movimento! Não é possível desligar!")

    # frear o carro
    def frear_carro(self):
        if self.ligado and self.velocidade > 0:
            self.velocidade -= 5
            if self.velocidade < 0:
                self.velocidade = 0
            print(
                f"O carro {self.modelo} freou. Velocidade atual: {self.velocidade} km/h")
        else:
            print(f"O carro {self.modelo} já está parado ou desligado!")

    # e tem que ter a inserção da  ativação da chave assim que o metodo abrir carro for True
    def ativar_chave(self):
        if self.aberto and not self.chave.ativa:
            self.chave.ativa = True
            print("Chave ativada!")
        else:
            print("Chave já está ativa ou o carro está fechado!")
# lucas
