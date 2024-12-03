class No:
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo

class FilaD:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0
    
    def inserir(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
        else:
            self.ult.prox = self.ult = No(valor, None) # A senquência de execução é IMPORTANTE!
        self.quant += 1
    
    def remover(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
        self.quant -= 1
    
    def ver_primeiro(self):
        return self.prim.info
    
    def esta_vazia(self):
        return self.quant == 0
    
    def show(self):
        aux = self.prim
        while aux != None:
            print(aux.info, end=' ')
            aux = aux.prox
        print()