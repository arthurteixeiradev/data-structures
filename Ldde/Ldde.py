class No:
    def __init__(self, anterior, valor, proximo):
        self.ant = anterior
        self.info = valor
        self.prox = proximo

class Ldde:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0
    
    def inserir_inicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
        
        else:
            # A ordem é importante!!
            self.prim.ant = self.prim = No(None, valor, self.prim)
        self.quant += 1

    def inserir_fim(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
        else:
            self.ult.prox = self.ult = No(self.ult, valor, None)
        self.quant += 1

    def remover_fim(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.ult = self.ult.ant
            self.ult.prox = None
        self.quant -= 1

    def remover(self, valor):
        if self.quant == 1 and self.prim.info == valor:
            self.prim = self.ult = None
            self.quant -= 1
        else:
            if self.prim.info == valor: # Caso seja o primeiro!
                self.prim = self.prim.prox
                self.prim.ant = None
                self.quant -= 1
            elif self.ult.info == valor: # Caso seja o ultimo!
                self.ult = self.ult.ant
                self.ult.prox = None
                self.quant -= 1
            else:
                aux = self.prim
                while aux != None and aux.info != valor: # A sequencia é importante!
                    aux = aux.prox
                
                if aux != None:
                    aux.ant.prox = aux.prox
                    aux.prox.ant = aux.ant
                    self.quant -= 1