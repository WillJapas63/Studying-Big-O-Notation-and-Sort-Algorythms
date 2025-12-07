def lines():
    print("------------------------------------")


def BubbleSort(lista):
    n = len(lista)  #Analisa o tamanho da lista
    for i in range (n): #Percorre cada elemento dela
        for j in range (0, n - 1 - i): #Começa no primeiro item, n-1 é o seguro que ela não vai estravazar, -i ignora o elemento que já esta certo
            if lista[j] > lista[j + 1]: #Se o elemento atual for maior que o segundo:
                lista [j], lista[j + 1] = lista[j + 1], lista [j] #Troque os elementos
                print(lista)
    return lista
               

               
def selection_sort(lista):
    n = len(lista) #Analisa o tamanho da lista
    for i in range (n): #Percorre cada elemento da lista
        indice_menor = i #Define indice_menor = 0 ou "i"

        for j in range (i + 1, n):      #Faz a comparação com todos os proximos numeros
            if lista [j] < lista [indice_menor]: #Se o numero comparado for menor
                indice_menor = j            #Ele se torna o menor numero então

    if indice_menor != i:
        lista [i], lista [indice_menor] = lista [indice_menor], lista [i]  #Faz as devidas trocas
        print(lista)
    return lista


def insertion_sort(lista):
    for i in range (1, len(lista)):     #Analista a lista, porém, inicialmente considera o segundo elemento
        chave = lista[i]                #define uma chave com o elemento "I" da lista, esse é o que queremos inserir (segundo elemento)
        j = i - 1                       #Compara com o elemento a esquerda

        while j >= 0 and lista[j] > chave:  #Enquanto "j" for maior ou igual a 0 (Impede o programa acessar indices negativos)
                                            #E enquanto lista[j] for maior que a chave, ou seja ele garante que só elementos maiores serão empurrados
            lista[j + 1] = lista[j]         #Se for verdade, ele move o maior elemento para a direita
            print(lista)
            j -= 1                          #Move para a esqueda para verificar o proximo elemento

        lista[j + 1] = chave                 #Quando o programa finaliza, J está parado a um ponto atrás do correto, então ele mira para J + 1 e insere
                                            #O valor da chave

    print (lista)                           
    return lista 



# O(1) — Tempo Constante
# O tempo de execução não cresce com o tamanho da entrada.
# Ex.: acessar lista[i], comparar duas variáveis, trocar dois valores.
# Executa sempre em tempo fixo, independentemente do tamanho da lista.

# O(n) — Tempo Linear
# O tempo cresce proporcionalmente ao tamanho da entrada.
# Ex.: percorrer uma lista uma vez (for item in lista).
# Cada elemento exige uma operação.

# O(n²) — Tempo Quadrático
# O tempo cresce proporcionalmente ao quadrado do tamanho da entrada.
# Ex.: loops aninhados que percorrem a lista dentro de outra passagem.
# Muito lento para listas grandes.

# O(log n) — Tempo Logarítmico
# O tempo cresce muito lentamente mesmo quando a entrada aumenta bastante.
# Ex.: busca binária, dividir a lista pela metade a cada passo.
# Excelente eficiência.

# O(n log n) — Tempo Quase Linear
# Usado pelos algoritmos de ordenação rápidos (QuickSort, MergeSort).
# A entrada é percorrida múltiplas vezes conforme ela é dividida em partes.
# Muito eficiente para ordenar listas grandes.

# O(2^n) — Tempo Exponencial
# O tempo dobra a cada elemento adicional.
# Ex.: certos algoritmos de recursão pesada, problemas de força bruta.
# Impraticável para entradas grandes.

# O(n!) — Tempo Fatorial
# Crescimento extremamente rápido.
# Ex.: gerar todas as permutações possíveis de uma lista.
# Quase nunca utilizável em aplicações reais.