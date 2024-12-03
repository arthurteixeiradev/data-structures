class Les:
    def __init__(self, tamanho):
        self.tam = tamanho
        self.array = [None] * tamanho
        self.qt = 0
   
    def inserirFim(self, valor):
        self.array[self.qt] = valor
        self.qt += 1
       
    def estaCheia(self):
        return self.qt == self.tam

    def estaVazia(self):
        return self.qt == 0

    def removerFim(self):
        self.qt -= 1

    def show(self):
        for i in range(self.qt):
            print(self.array[i], end=' ')
        print()

    def getQt(self):
        return self.qt

    def getPrim(self):
        return self.array[0]

    def getUlt(self):
        return self.array[self.qt - 1]
   
    def inserirInicio(self, valor):
        for i in range(self.qt, 0, -1):
            self.array[i] = self.array[i - 1]
       
        self.array[0] = valor
        self.qt += 1
   
    def removerInicio(self):
        for i in range(self.qt - 1):
            self.array[i] = self.array[i + 1]
        self.qt -= 1