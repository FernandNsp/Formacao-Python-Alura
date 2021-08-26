import random

def jogar():
   print("\n************************************")
   print("* Bem vindo ao jogo de Adivinhação *")
   print("************************************\n")

   numero_secreto = random.randrange(1, 101)
   total_de_tentativas = 0
   pontos = 1000

   print(">> Qual o nível de dificuldade?")
   print("(1) Fácil\n(2) Médio\n(3) Difícil")

   nivel = 0

   while(nivel == 0):
      nivel = int(input("- "))

      if(nivel == 1):
         total_de_tentativas = 20
      elif(nivel == 2):
         total_de_tentativas = 10
      elif(nivel == 3):
         total_de_tentativas = 5
      else:
         print("\n>> Nivel invalido, insira outro:\n")
         nivel = 0

   for rodada in range(1, total_de_tentativas + 1):
      print("\n>> Tentativa {} de {} <<\n" .format(rodada, total_de_tentativas))

      chute = int(input(">> Digite um número entre 1 e 100: "))

      if(chute < 1 or chute > 100):
         print("\n>> Número inválido! Insira um número entre 1 e 100!")
         continue

      acertou = chute == numero_secreto
      maior = chute < numero_secreto
      menor = chute > numero_secreto

      if(acertou):
         print("\n>> Parabéns! Você acertou e fez {} pontos!" .format(pontos))
         break
      else:
         if(maior):
            print("\n>> ERROU! Está frio, seu número foi MAIOR!")
         elif(menor):
            print("\n>> ERROU! Está frio, seu número foi MENOR!")
         
         pontos_perdidos = abs(numero_secreto - chute)
         pontos -= pontos_perdidos

   print("\n>> [FIM DE JOGO] <<\n\n")

if(__name__ == "__main__"):
   jogar()



