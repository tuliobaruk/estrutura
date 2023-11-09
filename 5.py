def quicksort(lista) -> list:
    if len(lista) == 0: 
        return lista
    pivo = lista[0]
    menor = quicksort([i for i in lista[1:] if i <= pivo])
    maior   = quicksort([i for i in lista[1:] if i > pivo])
    return menor + [pivo] + maior


listaUm = [int(i) for i in input().strip().split()] # Primeira lista de números inteiros
listaDois = [int(i) for i in input().strip().split()] # Segunda lista de números inteiros

listaMesclada = listaUm + listaDois
print(quicksort(listaMesclada))