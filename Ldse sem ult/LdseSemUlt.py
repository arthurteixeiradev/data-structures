class No:
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo


class Ldse:  #Sem o ult!!
    def __init__(self):
        self.prim = None
        self.quant = 0

    def inserirFim(self, valor):
        if self.quant == 0:
            self.prim = No(valor, None)
        else:
            aux = self.prim
            while aux.prox != None:
                aux = aux.prox
            aux.prox = No(valor, None)
        self.quant += 1

    def removerInicio(self):
        if self.quant == 1:
            self.prim = None
        else:
            self.prim = self.prim.prox
        self.quant -= 1
    
    def removerFim(self):
        if self.quant == 1:
            self.prim = None
            self.quant -= 1
        else:
            aux = self.prim
            ant = None
            while aux.prox != None:
                ant = aux
                aux = aux.prox
            
            ant.prox = aux.prox
            self.quant -= 1

    def show(self):
        aux = self.prim
        while aux != None:
            print(aux.info, end=' ')
            aux = aux.prox
        print()