class Automovel:
    def __init__(self, marca, modelo, chassi): # o primeiro argumento é sempre relacionado à instáncia, podemo chamar do que quiser, aqui chamamos de self
        self.marca = marca
        self.modelo = modelo
        self.chassi = chassi
    
    def rodas(self):
        if self.marca == "Gol":
            print("rodas de Gol")
        elif self.marca == "Tesla":
            print("rodas de Tesla")


auto0 = Automovel("Tesla","abc","5554ca58")
auto1 = Automovel("Gol","xyz","6886ghrt6")
auto0.rodas()
auto1.rodas()