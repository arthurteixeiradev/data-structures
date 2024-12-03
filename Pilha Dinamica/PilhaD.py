class No:
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo

class PilhaD:
    def __init__(self):
        self.topo = None
        self.quant = 0
    
    def push(self, valor):
        self.topo = No(valor, self.topo)
        self.quant += 1
    
    def pop(self):
        if not self.esta_vazia():
            self.topo = self.topo.prox
            self.quant -= 1
    
    def esta_vazia(self):
        return self.quant == 0
    
    def ver_topo(self):
        return self.topo.info
    
    def tamanho_atual(self):
        return self.quant

    def verifica_palindromo(self, palavra):
        pilha = PilhaD()
        tam_palavra = len(palavra)
        for i in range(tam_palavra):
            pilha.push(palavra[i])

        for i in range(tam_palavra):
            if pilha.ver_topo() != palavra[i]:
                return False
            pilha.pop()
        return True

    def valida_parenteses(self, expressao):
        p = PilhaD()
        for i in range(len(expressao)):
            if expressao[i] == '(':
                p.push('(')
            elif expressao[i] == ')':
                if p.esta_vazia():
                    return False
                p.pop()
        return p.esta_vazia()
    
    def verifica_parenteses2(self, expressao):
        pilha = PilhaD()
        for char in expressao:
            if char in '([{':
                pilha.push(char)
            elif char in ')]}':
                if pilha.esta_vazia():
                    return False
                topo = pilha.pop()
                if (char == ')' and topo != '(') or \
                    (char == ']' and topo != '[') or \
                    (char == '}' and topo != '{'):
                    return False
        return pilha.esta_vazia()
    
    def calculadora_posfixa(self, expressao):
        pilha = PilhaD()
        for token in expressao.split():
            if token.isdigit():
                pilha.push(float(token))
            else:
                b = pilha.ver_topo()
                pilha.pop()
                a = pilha.ver_topo()
                pilha.pop()
                if token == '+':
                    pilha.push(a + b)
                elif token == '-':
                    pilha.push(a - b)
                elif token == '*':
                    pilha.push(a * b)
                elif token == '/':
                    pilha.push(a / b)
        
        return pilha.ver_topo()
    
    def clear(self):
        """Esvazia a pilha."""
        self.topo = None
        self.quant = 0
    
    def get_elements(self):
        """Retorna uma lista com todos os elementos da pilha."""
        elementos = []
        atual = self.topo
        while atual is not None:
            elementos.append(atual.info)
            atual = atual.prox
        return elementos
    
    def reverse(self):
        """Inverte a ordem dos elementos na pilha."""
        elementos = self.get_elements()
        self.clear()
        for elemento in reversed(elementos):
            self.push(elemento)
    
    def show(self):
        aux = self.topo
        while aux is not None:
            print(aux.info, end=' ')
            aux = aux.prox
    
    def show_reverso(self):
        """Imprime os elementos da pilha em ordem inversa."""
        elementos = []
        atual = self.topo
        while atual is not None:
            elementos.append(atual.info)
            atual = atual.prox

        for elemento in reversed(elementos):
            print(elemento)