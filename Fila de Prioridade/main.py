import FilaP

fila = FilaP.FilaP()
fila.inserir('A', 2)
fila.inserir('B', 1)
fila.inserir('C', 3)
fila.inserir('D', 1)
fila.inserir('E', 2)
fila.inserir('F', 3)

fila.remover()
fila.remover()
fila.remover()
fila.remover()

fila.inserir('G', 1)

print(fila.ver_primeiro())