try:
    class Carro():
        def __init__(self, modelo, fabricante):
            self.modelo = modelo
            self.fabricante = fabricante
            self.__combustivel = 100
        
        @property
        def combustivel(self):
            return self.__combustivel

        @combustivel.setter
        def combustivel(self, valor):
            if valor < self.__combustivel:
                print("Valor de combustível mínimo invalido")
            else:
                self.__combustivel = valor

        def acelerar(self):
            if self.__combustivel <= 0:
                print("Sem combustivel")
            else:
                self.__combustivel -= 10
                print("Acelerando...")


    meu_carro = Carro("Opala", "Chevrolet")

    print(f"Fabricante: {meu_carro.fabricante}")
    print(f"Modelo: {meu_carro.modelo}")
    print(f"Combustivel: {meu_carro.__combustivel}")

    meu_carro.acelerar()

    print(f"Fabricante: {meu_carro.fabricante}")
    print(f"Modelo: {meu_carro.modelo}")
    print(f"Combustivel: {meu_carro.__combustivel}")
except Exception as e:
    print(f"Erro: {e}")