import FilaD

class FilaP:
    def __init__(self):
        self.F1 = FilaD.FilaD()
        self.F2 = FilaD.FilaD()
        self.F3 = FilaD.FilaD()
    
    def inserir(self, valor, prior):
        if prior == 1:
            self.F1.inserir(valor)
        elif prior == 2:
            self.F2.inserir(valor)
        else:
            self.F3.inserir(valor)
        
    def remover(self):
        if not self.F1.esta_vazia():
            self.F1.remover()
        elif not self.F2.esta_vazia():
            self.F2.remover()
        else:
            self.F3.remover()
    
    def ver_primeiro(self):
        if not self.F1.esta_vazia():
            return self.F1.ver_primeiro()
        elif not self.F2.esta_vazia():
            return self.F2.ver_primeiro()
        else:
            return self.F3.ver_primeiro()
    
    def esta_vazia(self):
        return self.F1.esta_vazia() and self.F2.esta_vazia() and self.F3.esta_vazia()
    
    def show(self):
        self.fila4.show()
        self.fila3.show()
        self.fila2.show()
        self.fila1.show()