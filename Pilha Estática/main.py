import PilhaE

'''string = "arara"
p = PilhaE.PilhaE(len(string))

if p.palindromo(string):
    print(f'A string "{string}" é um palíndromo.')
else:
    print(f'A string "{string}" não é um palíndromo.')


p.push('A')
p.push('B')
print(p.ver_topo())'''

c = PilhaE.PilhaE(10)
resultado = c.calcular_rpn("3 4 + 2 *")
if resultado is not None:
    print(f'Resultado da expressão: {resultado}')  # Saída: Resultado da expressão: 14