class No:
    def __init__(self, valor, proximo, anterior):
        self.info = valor
        self.prox = proximo
        self.ant = anterior

class Lddec:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0
    
    def inserir_inicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
            self.prim.ant = self.ult.prox = self.prim
        else:
            self.prim.ant = self.prim = No(self.ult, valor, self.prim)
            self.ult.prox = self.prim
        self.quant += 1
    
    def remover_inicio(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
            self.prim.ant = self.ult
            self.ult.prox = self.prim
        self.quant -= 1
    
    def inserir_fim(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor)
            self.prim.ant = self.ult.prox = self.prim
        else:
            self.ult.prox = self.ult = No(self.ult, valor, self.prim)
            self.prim.ant = self.ult
        self.quant += 1
    
    def remover_fim(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.ult = self.ult.ant
            self.ult.prox = self.prim
            self.prim.ant = self.ult
        self.quant -= 1
    
    def show(self):
        aux = self.prim
        for i in range(self.quant):
            print(aux.info, end=" ")
            aux = aux.prox
        print("\n")
    
    def show_inverso(self):
        aux = self.ult
        for i in range(self.quant):
            print(aux.info, end=' ')
            aux = aux.ant
        print('\n')
    
    def estaVazia(self):
        return self.quant == 0
    
    def tamanho_atual(self):
        return self.quant
    
    def ver_primeiro(self):
        return self.prim.info
    
    def ver_ultimo(self):
        return self.ult.info