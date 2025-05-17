class Veiculo():
    def __init__(self, modelo, fabricante):
        self.modelo = modelo
        self.fabricante = fabricante

    def acelerar(self):
        print(F"Acelerando... {self.modelo} na estrada")

class Moto(Veiculo):
    pass

class Carro(Veiculo):
    pass

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

