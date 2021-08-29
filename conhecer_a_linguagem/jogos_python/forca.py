import random

def clear_console():
   import os
   os.system('cls' if os.name == 'nt' else 'clear')

def imprime_abertura():
   clear_console()
   print("\n************************************")
   print("*    Bem vindo ao Jogo da Forca    *")
   print("************************************\n")

def carrega_palavra_secreta():
   arquivo = open("palavras.txt", "r")
   palavras = []

   with open(palavras.txt) as arquivo: # sintaxe para fazer com que o arquivo seja fechado corretamente
      for linha in arquivo:
         linha = linha.strip()
         palavras.append(linha)
      
   numero = random.randrange(0, len(palavras)) # palavra aleatoria (de 0 ao tamanho da lista)
   palavras_secreta = palavras[numero].upper() # deixar a palavra sorteada em maiusculo

def underline_letras(palavra):
   return ["_" for letra in palavra]

def pede_chute():
   chute = input(">> Insira uma letra: ")
   chute = chute.strip().upper # remove espaços e transforma em maiuscula
   return chute

def chute_correto(chute, letras_acertadas, palavra_secreta):
   index = 0

   # verificar se a letra inserida existe na palavra secreta
   for letra in palavra_secreta:
         if(chute == letra):
            letras_acertadas[index] = letra
         index += 1

def desenha_forca(erros):
   clear_console()
   print("\n  _______     ")
   print(" |/      |    ")

   if(erros == 1):
      print (" |      (_)   ")
      print (" |            ")
      print (" |            ")
      print (" |            ")

   if(erros == 2):
      print (" |      (_)   ")
      print (" |      /     ")
      print (" |            ")
      print (" |            ")

   if(erros == 3):
      print (" |      (_)   ")
      print (" |      /|    ")
      print (" |            ")
      print (" |            ")

   if(erros == 4):
      print (" |      (_)   ")
      print (" |      /|\   ")
      print (" |            ")
      print (" |            ")

   if(erros == 5):
      print (" |      (_)   ")
      print (" |      /|\   ")
      print (" |       |    ")
      print (" |            ")

   if(erros == 6):
      print (" |      (_)   ")
      print (" |      /|\   ")
      print (" |       |    ")
      print (" |      /     ")

   if(erros == 7):
      print (" |      (_)   ")
      print (" |      /|\   ")
      print (" |       |    ")
      print (" |      / \   ")

   print(" |            ")
   print("_|___         ")
   print()

def vencedor():
   print("\n>> Parabéns! Você ganhou!\n")
   print("       ___________      ")
   print("      '._==_==_=_.'     ")
   print("      .-\\:      /-.    ")
   print("     | (|:.     |) |    ")
   print("      '-|:.     |-'     ")
   print("        \\::.    /      ")
   print("         '::. .'        ")
   print("           ) (          ")
   print("         _.' '._        ")
   print("        '-------'       ")

def perdedor(palavra_secreta):
   print("\n>> Que pena, você perdeu!\n>> A palavra secreta era [{}].\n".format(palavra_secreta))
   print("    _______________         ")
   print("   /               \       ")
   print("  /                 \      ")
   print("//                   \/\  ")
   print("\|   XXXX     XXXX   | /   ")
   print(" |   XXXX     XXXX   |/     ")
   print(" |   XXX       XXX   |      ")
   print(" |                   |      ")
   print(" \__      XXX      __/     ")
   print("   |\     XXX     /|       ")
   print("   | |           | |        ")
   print("   | I I I I I I I |        ")
   print("   |  I I I I I I  |        ")
   print("   \_             _/       ")
   print("     \_         _/         ")
   print("       \_______/           ")

      
def jogar():
   imprime_abertura()

   

if(__name__ == "__main__"):
   jogar()
