class FileE:
    def __init__(self, tamanho):
        self.tam = tamanho
        self.vetor = [None] * tamanho
        self.quant = 0

    def inserir(self, valor):
        self.vetor[self.quant] = valor
        self.quant += 1
    
    def remover(self):
        for i in range(self.quant - 1):
            self.vetor[i] = self.vetor[i + 1]
        self.quant -= 1

    def ver_primeiro(self):
        return self.vetor[0]
    
    def estaCheia(self):
        return self.quant == self.tam
    
    def estaVazia(self):
        return self.quant == 0
    
    def show(self):
        for i in range(self.quant):
            print(self.vetor[i], end=' ')
        print()