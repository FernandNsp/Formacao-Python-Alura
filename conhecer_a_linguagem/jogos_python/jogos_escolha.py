import forca
import adivinhacao

print("\n************************************")
print("*         Escolha de Jogos         *")
print("************************************\n")

print("(1) Forca\n(2) Adivinhação")
jogo = int(input("\n>> Insira o jogo desejado:\n- "))

if(jogo == 1):
   forca.jogar()
elif(jogo == 2):
   adivinhacao.jogar()
