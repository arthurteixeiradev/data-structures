class Lescircular:
    def __init__(self, tamanho):
        self.tam_maximo = tamanho
        self.vetor = [None] * tamanho
        self.inicio = 0
        self.fim = 0
        self.quant = 0

    def inserir_fim(self, valor):
        self.vetor[self.fim] = valor
        self.fim = (self.fim + 1) % self.tam_maximo
        self.quant += 1
    
    def remover_fim(self):
        self.fim = (self.fim - 1) % self.tam_maximo
        self.quant -= 1
    
    def inserir_inicio(self, valor):
        self.inicio = (self.inicio - 1) % self.tam_maximo
        self.vetor[self.inicio] = valor
        self.quant += 1
    
    def remover_inicio(self):
        self.inicio = (self.inicio + 1) % self.tam_maximo
        self.quant -= 1
    
    def esta_vazia(self):
        return self.quant == 0

    def esta_cheia(self):
        return self.quant == self.tam_maximo

    def show(self):
        for i in range(self.quant):
            print(self.vetor[(self.inicio + i)%self.tam_maximo],end=' ')
        print()
    
    def ver_primeiro(self):
        return self.vetor[self.inicio]

    def ver_ultimo(self):
        return self.vetor[(self.fim - 1) % self.tam_maximo] 