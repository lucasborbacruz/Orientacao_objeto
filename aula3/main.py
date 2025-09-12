from car import Chave
from car import Car

ch = Chave("Fiat")
ch1 = Chave("Chevrolet")

car1 = Car("uno", 1998, "verde", 1.0, "ABC-1234", ch)

car1.abrir_carro(ch)

car1.ligar_carro()

# Acelerar o carro
for i in range(5):
    car1.acelerar_carro()

print(car1.chave.marca)
# Frear o carro
for i in range(6):
    car1.frear_carro()
# Desligar o carro
car1.desligar_carro()
car1.frear_carro()
