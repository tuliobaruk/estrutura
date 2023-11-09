lista = [int(i) for i in input().strip().split()] # Lista de números inteiros
listaFiltrada = [i for i in lista if i % 2 == 0]
print(listaFiltrada)