class No:
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo

class Lee:
    def __init__(self,tamanho):
        self.tam_maximo = tamanho
        self.vetor = [None] * self.tam_maximo
        self.quant = 0
        self.prox_pos_vazia = self.inicializa_estrutura()
        self.prim = -1
        self.ult = -1

    def inicializa_estrutura(self):
        for i in range(self.tam_maximo-1):
            self.vetor[i] = No(None,i+1)
        self.vetor[self.tam_maximo-1] = No(None,-1)
        return 0
    
    def ocupa_no(self,valor,proximo):
        posicao_livre = self.prox_pos_vazia
        self.prox_pos_vazia = self.vetor[self.prox_pos_vazia].prox
        self.vetor[posicao_livre] = No(valor,proximo)
        return posicao_livre
    
    def inserir_inicio(self,valor):
        if self.quant == 0:
            self.prim = self.ult = self.ocupa_no(valor,-1)
            self.quant += 1
        else:
            self.prim = self.ocupa_no(valor,self.prim)
        self.quant += 1
    
    def show(self):
        aux = self.prim
        while aux != -1:
            print(self.vetor[aux].info)
            aux = self.vetor[aux].prox
        
    def show_vetor(self):
        print('Prim=',self.prim)
        print('Ult=',self.ult)
        print('Primeira pos vazia=',self.prox_pos_vazia)
        print('Vetor=')
        for i in range(self.tam_maximo):
            print(i, self.vetor[i].info, self.vetor[i].prox)

    def devolve_no(self, no):
        self.vetor[no].prox = self.prox_pos_vazia
        self.prox_pos_vazia = no
    
    def remover_fim(self):
        if self.quant == 1:
            self.devolve_no(self.prim)
            self.prim = self.ult = -1
        else:
            aux = self.prim
            for i in range(self.quant-2):
                aux = self.vetor[aux].prox
            self.devolve_no(self.ult)
            self.vetor[aux].prox = -1
            self.ult = aux
        self.quant-=1
    
    def remover_inicio(self):
        if self.quant == 1:
            self.devolve_no(self.prim)
            self.prim = self.ult = -1
        else:
            novo_prim = self.vetor[self.prim].prox
            self.devolve_no(self.prim)
            self.prim = novo_prim
        self.quant-=1
    
    def remover_irmaos(self,valor):
        if self.quant !=1 and self.quant !=0:
            anterior_do_anterior = -1
            anterior = -1
            atual = self.prim
            while self.vetor[atual].info != valor and atual != -1:
            # andando pela lista até achar valor
            # # ou chegar ao fim da lista
                anterior_do_anterior = anterior
                anterior = atual
                atual = self.vetor[atual].prox
            if self.vetor[atual].info == valor:
            # ou seja, achou valor na lista e ele está no índice atual
                if self.vetor[self.prim].prox == atual:
                # age se o irmão anterior for o primeiro da lista
                    self.remover_inicio()
                else:
                    if atual != self.prim:
                    # caso o irmão anterior não seja o primeiro da lista
                        self.vetor[anterior_do_anterior].prox = atual
                        self.devolve_no(anterior)
                        self.quant -= 1
                if self.vetor[atual].prox == self.ult:
                # age se o irmão posterior for o próximo da lista
                    self.remover_fim()
                else:
                    if atual != self.ult:
                    # caso o irmão posterior não seja o primeiro da lista
                        proximo = self.vetor[atual].prox
                        self.vetor[atual].prox = self.vetor[proximo].prox
                        self.devolve_no(proximo)
                        self.quant -= 1