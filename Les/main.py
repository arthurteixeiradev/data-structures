import Les


l = Les.Les(5)


l.inserirFim('A')
l.inserirFim('B')
l.inserirFim('C')
print('Antes de remover fim')
l.show()
print('Depois de remover fim')
l.removerFim()
l.show()
print('Depois de inserir fim')
l.inserirFim('D')
l.show()
l.inserirInicio('Y')
l.show()
l.removerInicio()
l.show()
