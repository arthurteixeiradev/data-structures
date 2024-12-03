class No:
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo


class Ldse:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0

    def inserirInicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
        else:
            self.prim = No(valor, self.prim)
        self.quant += 1

    def show(self):
        aux = self.prim
        while aux != None:
            print(aux.info, end=' ')
            aux = aux.prox
        print()

    def removerInicio(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
        self.quant -= 1
   
    def inserirFim(self, valor): # Fazer essa função sem o atributo fim!
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
        else:
            self.ult.prox = self.ult = No(valor, None) # A senquência de execução é IMPORTANTE!
        self.quant += 1
   
    def removerFim(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            aux = self.prim
            while aux.prox != self.ult: # Essa condição é muito IMPORTANTE!
                aux = aux.prox
            self.ult = aux
            self.ult.prox = None
        self.quant -= 1

    def remover(self, valor):
        if self.quant == 1 and self.prim.info == valor:
            self.prim = self.ult = None
            self.quant -= 1
        else:
            if self.prim.info == valor:
                self.prim = self.prim.prox
                self.quant -= 1
            elif self.ult.info == valor:
                aux = self.prim
                while aux.prox != self.ult:
                    aux = aux.prox
                self.ult = aux
                self.ult.prox = None
                self.quant -= 1
            else:
                aux = self.prim
                ant = None
                while aux != None and aux.info != valor: # (aux.info != valor and aux != None) essa ordem vai dar error!!
                    ant = aux
                    aux = aux.prox
                if aux != None:
                    ant.prox = aux.prox
                    self.quant -= 1