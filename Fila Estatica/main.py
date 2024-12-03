import FilaE

l = FilaE.FileE(5)

l.inserir('A')
l.inserir('B')
print('Depois de inserir A, B')
l.show()
l.remover()
l.show()
l.inserir('C')
l.show()