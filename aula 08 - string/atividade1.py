#Escreva um programa que lê uma frase, uma palavra antiga
#e uma palavra nova. O programa deve imprimir a frase com ocorrencias
#da palavra antiga substituidas pela palavra nova.

frase = input("Digite uma frase: ")
palavra_antiga = input("Digite a palavra antiga: ")
palavra_nova = input("Digite a palavra nova: ")

palavras = frase.sprit()
for i in range(len(palavras)):
    if palavras[i] == palavra_antiga:
        palavras[i] = palavra_nova
    
resultado = (palavras)
print("Resultado:", resultado)