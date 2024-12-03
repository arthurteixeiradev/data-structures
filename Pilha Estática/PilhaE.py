class PilhaE:
    def __init__(self, tamanho):
        self.tam = tamanho
        self.array = [None] * tamanho
        self.quant = 0

    def push(self, valor):
        self.array[self.quant] = valor
        self.quant += 1
    
    def pop(self):
        self.quant -= 1
    
    def ver_topo(self):
        return self.array[self.quant - 1]

    def esta_vazia(self):
        return self.quant == 0

    def esta_cheia(self):
        return self.quant == self.tam
    
    def palindromo(self, s):
        s = s.replace(" ", "").lower()

        for letra in s:
            self.push(letra)
        
        for letra in s:
            if letra != self.ver_topo():
                return False
            self.pop()
        
        return self.esta_vazia()
    
    def imprimir(self):
        for i in range(self.quant):
            print(self.array[i], end=" ")
        print()
    
    def buscar(self, valor):
        for i in range(self.quant):
            if self.array[i] == valor:
                return True
        return False
    
    def limpar(self):
        self.quant = 0
    
    def inverter(self):
        pilha_aux = PilhaE(self.tam)
        while not self.esta_vazia():
            pilha_aux.push(self.pop())
        self.array = pilha_aux.array
        self.quant = pilha_aux.quant