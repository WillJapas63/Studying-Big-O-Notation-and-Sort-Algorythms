import random
import funções


funções.lines()
print("|Aqui estão seus numeros iniciais: |")
lista = [0,1,2,3,4,5,6,7,8,9,10]
print(f"|{lista}|")
funções.lines()

print ("")

funções.lines()
print("|E aqui vamos começar o jogo:      |")
random.shuffle(lista)
print(f"|{lista}|")
funções.lines()

print("1. Bubble Sort")
print("2. Selection Sort")
print("3. Insertion Sort")


numero_de_entrada= input('Coloque a ação que você deseja tomar: ')


#O(n²) Algorhytms
if (numero_de_entrada == '1'):
    funções.BubbleSort(lista)
elif(numero_de_entrada == '2'):
    funções.selection_sort(lista)
elif(numero_de_entrada == '3'):
    funções.insertion_sort(lista)
