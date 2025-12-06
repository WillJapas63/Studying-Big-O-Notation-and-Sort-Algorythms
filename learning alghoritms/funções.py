def lines():
    print("------------------------------------")


def BubbleSort(lista):
    n = len(lista)  #Analisa o tamanho da lista
    for i in range (n): #Percorre cada elemento dela
        for j in range (0, n - 1 - i): #Começa no primeiro item, n-1 é o seguro que ela não vai estravazar, -i ignora o elemento que já esta certo
            if lista[j] > lista[j + 1]: #Se o elemento atual for maior que o segundo:
                lista [j], lista[j + 1] = lista[j + 1], lista [j] #Troque os elementos
                print(lista)
               





               
def selection_sort(lista):
    n = len(lista) #Analisa o tamanho da lista
    for i in range (n): #Percorre cada elemento da lista
        indice_menor = i #Define indice_menor = 0 ou "i"

        for j in range (i + 1, n):      #Faz a comparação com todos os proximos numeros
            if lista [j] < lista [indice_menor]: #Se o numero comparado for menor
                indice_menor = j            #Ele se torna o menor numero então

        lista [i], lista [indice_menor] = lista [indice_menor], lista [i]  #Faz as devidas trocas
        print(lista)