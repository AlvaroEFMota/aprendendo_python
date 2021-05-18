class Animal:
    def __init__(self, tamanho, peso):
        self.tamanho = tamanho
        self.peso = peso
    
    def Informacoes(self):
        return "Tamanho: " + str(self.tamanho) + ", Peso:" + str(self.peso)


class Voador(Animal):
    def __init__(self, tamanho, peso, velocidade_voo):
        super().__init__(tamanho, peso)
        self.velocidade_voo = velocidade_voo

    def Informacoes(self):
        return super().Informacoes() + ", Velocidade de Voo: " + str(self.velocidade_voo)


voador = Voador(10,5,50)

print(voador.Informacoes())