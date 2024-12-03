class No:
    def __init__(self, anterior, valor, proximo):
        self.ant = anterior
        self.info = valor
        self.prox = proximo

class Lddec:
    def __init__(self):
        self.prim = None
        self.quant = 0

    def inserir_inicio(self,valor):
        if self.quant == 0:
            self.prim = No(None,valor,None)
            self.prim.ant = self.prim.prox = self.prim
        else:
            self.prim.ant = self.prim = No(self.prim, valor, self.prim)
        self.quant +=1

    def show_reverso(self):
        aux = self.prim
        for i in range(self.quant):
            print(aux.ant.info,end='')
            aux = aux.ant
        print()

    def show_normal(self):
        aux = self.prim
        for i in range(self.quant):
            print(aux.info,end='')
            aux = aux.prox
        print()