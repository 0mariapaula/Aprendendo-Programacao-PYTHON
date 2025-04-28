from random import randint

compuu = randint(0,5) # MEIO QUE FEZ O COMPUTADOR PENSAR
jogador = int (input("Em que numero você pensou? "))

if (compuu > jogador):
    print("O meu numero foi esse {} entao voce perdeu :(" .format(compuu))
else:
    print("O meu numero foi esse {} entao voce ganhou :)" .format(compuu))



