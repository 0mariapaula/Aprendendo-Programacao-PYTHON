#Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira. 
#import math #Aqui ele esta usando a "biblioteca toda"
#num = float (input('DIGITE UM NUMERO'))
#print('O VALOR FOI{} E A SUA PARTE INTEIRA FOI {}'.format(num,math.trunc(num)))

from math import trunc #Aqui ele esta usando a "biblioteca toda"
num = float (input('DIGITE UM NUMERO'))
print('O VALOR FOI{} E A SUA PARTE INTEIRA FOI {}'.format(num,trunc(num)))
