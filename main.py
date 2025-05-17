try:
    class Carro():
        def __init__(self, modelo, fabricante):
            self.modelo = modelo
            self.fabricante = fabricante
            self.combustivel = 100

        def acelerar(self):
            if self.combustivel <= 0:
                print("Sem combustivel")
            else:
                self.combustivel -= 10
                print("Acelerando...")

    meu_carro = Carro("Opala", "Chevrolet")

    print(f"Fabricante: {meu_carro.fabricante}")
    print(f"Modelo: {meu_carro.modelo}")
    print(f"Combustivel: {meu_carro.combustivel}")

    meu_carro.acelerar()
    print(f"Fabricante: {meu_carro.fabricante}")
    print(f"Modelo: {meu_carro.modelo}")
    print(f"Combustivel: {meu_carro.combustivel}")
except Exception as e:
    print(f"Erro: {e}")