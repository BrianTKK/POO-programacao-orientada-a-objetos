from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, modelo, fabricante):
        self.modelo = modelo
        self.fabricante = fabricante

    @abstractmethod
    def acelerar(self):
        pass

class Moto(Veiculo):
    def acelerar(self):
        print(F"Vrroom... {self.modelo} na estrada")

class Carro(Veiculo):
    def acelerar(self):
        print(F"grugrugru... {self.modelo} dando partida.")
        print(F"{self.modelo} na estrada!.")

class Aviao(Veiculo):
    def acelerar(self):
        print(F"Fiuuuuu... {self.modelo} nos ares!")

class Barco(Veiculo):
    def acelerar(self):
        print(F"Splash... {self.modelo} na agua!")

meu_carro = Carro("Opala", "Chevrolet")
meu_carro.acelerar()

minha_moto = Moto("ZX4R", "Kawasaki")
minha_moto.acelerar()

meu_aviao = Aviao("Boeing 777", "FAB")
meu_aviao.acelerar()

meu_barco = Barco("Barco A", "FAB")
meu_barco.acelerar()

