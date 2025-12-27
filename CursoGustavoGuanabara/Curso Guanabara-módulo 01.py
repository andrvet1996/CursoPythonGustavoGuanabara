#PRIMEIROS COMANDOS

#DESAFIO 1
#nome = input ('Qual é o seu nome?')
#print ("Olá",nome,'!','Prazer em te conhecer!')

#DESAFIO 2
#dia = input ('Em que dia você nasceu?')
#mês = input ('Em que mês você nasceu (escreva o mês)?')
#ano = input ('Em que ano você nasceu?')
#print ('Você nasceu no dia', dia, "do", mês, 'de', ano,'. Correto?')

#DESAFIO 3
#n1 = eval (input ('Digite o primeiro número:'))
#n2 = eval (input ('Digite o segundo número:'))
#soma = n1 + n2
#print ('A soma é', soma,'.')

#EXERCÍCIO 2 (parece o desafio 1)
#nome = input ('Digite seu nome: ')
#print ('É um prazer te conhecer, {}!'.format(nome)) 


#TIPOS PRIMITIVOS (int, float, bool=True or False, str)
#Exemplo 1
#n1 = int (input ('Digite o primeiro número:'))
#n2 = int (input ('Digite o segundo número:'))
#s = n1+n2
#print ('A soma entre', n1, 'e', n2, 'vale', s) 

#Desafio 2 is. alguma coisa
#n = input ('Digite algo:')
#print (n.isnumeric()) #confira se é inteiro
#print (n.isalpha())#confirma se é letra
#print (n.isalnum())#confirma se é letra e número 3a por exemplo
#print (n.isupper())

#Desafio 3 soma de números e apresentar resultado
n1 = int (input ('Digite o primeiro número: '))
n2 = int (input ('Digite o segundo número:  '))
n3 = int (input ('Digite o terceiro número: '))
s = n1+n2+n3
print ('A soma de {}, {} e {} é {}'. format (n1, n2, n3, s))

#EXERCÍCIO 4 dissecando uma variável
#a = input ('Digite algo: ')
#print ('O tipo primitivo desse valor é', type(a))
#print ('Só possui espaço?', a.isspace())
#print ('É um número?', a.isnumeric())
#print ('É alfabético?', a.isalpha())
#print ('É alfanumérico?', a.isalnum())
#print ('Está em maiúscula?', a.isupper())
#print ('Está em minúscula?', a.islower())
#print ('Está capitalizada?', a.istitle())#só primeira letra maiúscula

#Outra forma de fazer
a = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(a)}')
print(f'Só há espaços? {a.isspace()}')
print(f'É um número? {a.isnumeric()}')
print(f'É alfabético? {a.isalpha()}')
print(f'É alfanumérico? {a.isalnum()}')
print(f'Todas as letras são maiúsculas? {a.isupper()}')
print(f'Todas as letras são minúsculas? {a.islower()}')
print(f'Está capitalizada? {a.istitle()}')

#OPERADORES ARITMÉTICOS
#a = 2**3
#a = pow (2,3) isso é igual a 2**3
#print (a)

#raiz quadrada
#a = 25**(1/2)
#print (a)

#raiz cúbica
#a = 27**(1/3)
#print (a)

#nome = input ('Qual é o seu nome? ')
#print ('Prazer em conhecê-lo {:=^20}!'.format(nome))
# {:20} em 20 espaços 
# {:>20} em 20 espaços a direita
# {:<20} em 20 espaços a esquerda
# {:^20} em 20 espaços centralizado
# {:=^20} em 20 espaços centralizado com símbolo = ou outro que vc escolher

#n1 = int (input ('Digite o primeiro número: '))
#n2 = int (input ('Digite o segundo número: '))
#s = n1 + n2
#m = n1 * n2
#d = n1 / n2
#di = n1 // n2
#e = n1 ** n2

#print ('A soma é {}, o produto é {} e a divisão é {}.'. format (s, m, d), end=' ')
#end='' comando para não quebrar linha nos print
#print ('A soma é {}, o produto é {} e a divisão é {:.2f}.'. format (s, m, d))
#na divisão vai aparecer duas casas decimais
#print ('A divisão inteira é {} e a potência é {}.'. format (di, e))

#Desafio 5 sucessor e antecessor
n = int (input ('Escolha um número inteiro: '))
n1 = n - 1
n2 = n + 1
print ('O seu antecessor é {} e o sucessor é {}.'.format (n1, n2))
#print ('A soma entre {} e {} vale {}'.format(n1, n2, s))#outra forma

#outra forma de fazer, sem criar variáveis
n = int (input('Digite um número: '))
print ('Analisando o valor {}, seu antecessor é {} e o sucessor é {}.'.format (n, (n-1), (n+1)))

#Desafio 6 
#n = int (input ('Digite um número: '))
#dn = n * 2
#tn = n * 3
#rqn = n ** (1/2)
#print ('O dobro do número, o triplo e a raiz quadrada são, respectivamente {}, {} e {}.'.format (dn, tn, rqn))

#Desafio 7
#n1 = int (input ('Nota 1: '))
#n2 = int (input ('Nota 2: '))
#M = (n1 + n2) / 2
#print ('A média do aluno é {}.'. format (M))

#Desafio 8

m = int (input ('Digite o valor em metros: ')) 
cm = m * 100
mm = cm * 10
print ('O valor em centrímetros e milímetros são, respectivamente, {}cm e {}mm.'. format (cm, mm))

#Desafio 9 tabuada
n = int (input ('Digite um número: '))
n1 = n * 1
n2 = n * 2
n3 = n * 3
n4 = n * 4
n5 = n * 5
n6 = n * 6
n7 = n * 7
n8 = n * 8
n9 = n * 9
n10 = n * 10
print ('A tabuada no número digitado e: {},{},{},{},{},{},{},{},{},{}.'
.format (n1,n2,n3,n4,n5,n6,n7,n8,n9,n10))

#outra forma, sem criar vriáveis
n = int (input ('Digite um número para ver sua tabuada: '))
print ('*' * 12)
print ('{} * {:2} = {}'.format (n, 1, n*1))
print ('{} * {:2} = {}'.format (n, 2, n*2))
print ('{} * {:2} = {}'.format (n, 3, n*3))
print ('{} * {:2} = {}'.format (n, 4, n*4))
print ('{} * {:2} = {}'.format (n, 5, n*5))
print ('{} * {:2} = {}'.format (n, 6, n*6))
print ('{} * {:2} = {}'.format (n, 7, n*7))
print ('{} * {:2} = {}'.format (n, 8, n*8))
print ('{} * {:2} = {}'.format (n, 9, n*9))
print ('{} * {:2} = {}'.format (n, 10, n*10))
print ('*' * 12)

#Desafio 10 conversão real/dólar
r = eval (input('Quantos reais você possui? R$ '))
d = r / 3.27
print ('A sua quantia reais corresponde a {:.2f} dólares.'. format (d))

#Desafio 11 área para pintar
l = eval (input ('Qual a largura em metros? '))
h = eval (input ('Qual a altura em metros? ')) 
a = l * h
qt = a / 2
print ('Sua parede possui a área de {:.1f} metros quadrados.'.format (a))
print ('A quantidade de tinta utilizada será de {:.1f} litros.'.format (qt))

#Desafio 12 desconto
p = eval (input ('Digite o preço atual: R$ '))
npcd = p - (p * 0.05)
print ('O preço com desconto de 5% é R${:.2f}.'.format (npcd))

#Desafio 13 reajuste salarial
s = eval (input ('Digite seu salário atual: '))
ns = s + (s * 0.15)
print ('Seu salário com o aumento de 15% é R$ {:.2f}.'.format (ns))

#Exercício 14-conversão temperatura
c = eval (input('Digite a temperatura em ºC: '))
f = 32 + 1.8 * c
k = c + 273
print ('A temperatura {}ºC corresponde a {:.1f}ºF e {:.1f}K.'.format (c, f, k))

#Exercício 15-custo aluguel de carro
d = eval (input ('Quantos dias você ficou com o carro? '))
q = eval (input('Quantos quilometros você percorreu? '))
p = (60 * d) + (0.15 * q)
print ('O total a pagar é R${:.2f}.'.format (p))


#Aula 8- comandos math e random
#import math #impora tudo
#n = eval (input ('Digite um número: '))
#raiz = math.sqrt (n)
#print ('A raiz quadrada de {} é {:.3f}.'.format (n, raiz))

#from math import sqrt
#n = eval (input ('Digite um número: '))
#raiz = sqrt(n)
#print ('A raiz quadrada de {} é {:.2f}.'.format (n, raiz))

#import random  # gera número aleatório
#n = random.random()
#print(n)

#import random
#n = random.randint (1,10)#randint gera aleatórios dentro de um intervalo
#print(n)

import emoji   #importar emoji                                                    
print(emoji.emojize('Olá, mundo: sunglasses:', use_aliases=True))

import math
n = eval (input ('Digite um número decimal: '))
n = math.trunc(n)
print ('A porçaõ inteira do número é {}.'.format (n))

#Desafio 16-comando trunc 
from math import trunc
n = eval (input ('Digite um número decimal: '))
n = trunc(n)
print ('A porção inteira do número é {}.'.format (n))

import math
n = eval (input('Digite um número decimal: '))
print ('A parte inteira do número digitado é {}.'.format (math.trunc(n)))

from math import trunc 
n = eval (input('Digite um número decimal: '))
print ('A parte inteira do número digitado é {}.'.format (trunc (n)))

n = eval (input('Digite um número decimal: '))
print ('A parte inteira do número digitado é {}.'.format (int (n)))

#Desafio 17-cálculo hipotenusa
import math 
a = eval (input ('Digite um cateto: '))
b = eval (input ('Digite o outro cateto: '))
h = math.sqrt (a**2 + b**2)
print ('A hipotenusa é {}.'.format(h))

from math import sqrt
a = eval (input ('Digite um cateto: '))
b = eval (input ('Digite o outro cateto: '))
h = sqrt (a**2 + b**2)
print ('A hipotenusa é {}.'.format(h))

a = eval (input ('Digite um cateto: '))
b = eval (input ('Digite o outro cateto: '))
h = (a**2 + b**2) ** 0.5
print ('A hipotenusa é {}.'.format(h))

import math 
a = eval (input ('Digite um cateto: '))
b = eval (input ('Digite o outro cateto: '))
h = math.hypot (a, b)
print ('A hipotenusa é {:.2f}.'.format(h))

from math import hypot
a = eval (input ('Digite um cateto: '))
b = eval (input ('Digite o outro cateto: '))
h = hypot (a, b)
print ('A hipotenusa é {:.2f}.'.format(h))

#Desafio 18-calcular seno, cosseno e tangente 
from math import radians, sin, cos, tan
ângulo = eval (input('Digite o valor de um ângulo em graus: '))
seno = sin (radians (ângulo))
cosseno = cos (radians (ângulo))
tangente = tan (radians (ângulo))
print ('O seno, o cosseno e tangente do ângulo {} são, respectivamente, {:.2f}, {:.2f} e {:.2f}.'
.format(ângulo, seno, cosseno, tangente))

#Desafio 19 escolher um aluno de uma lista
import random
a1 = str (input ('Primeiro aluno: '))
a2 = str (input ('Segundo aluno: '))
a3 = str (input ('Terceiro aluno: '))
a4 = str (input ('Quarto aluno: '))
lista = [a1, a2, a3, a4]
escolhido = random.choice (lista)#comando choice escolhe um aluno
print ('O aluno escolhido foi {}'.format(escolhido))

#outra forma de fazer
from random import choice
a1 = str (input ('Primeiro aluno: '))
a2 = str (input ('Segundo aluno: '))
a3 = str (input ('Terceiro aluno: '))
a4 = str (input ('Quarto aluno: '))
lista = [a1, a2, a3, a4]
escolhido = choice (lista)
print ('O aluno escolhido foi {}'.format(escolhido))

#Desafio 20-embaralhar aluno commando Shuffle
#Desafio 20 embaralhar alunos para escolher
import random
a1 = str (input ('Primeiro aluno: '))
a2 = str (input ('Segundo aluno: '))
a3 = str (input ('Terceiro aluno: '))
a4 = str (input ('Quarto aluno: '))
lista = [a1, a2, a3,a4]
escolhido = random.shuffle (lista)#comando shuffle embaralha
print ('A ordem de apresentação será: ')
print (lista)

#outra forma de fazer
from random import shuffle
a1 = str (input ('Primeiro aluno: '))
a2 = str (input ('Segundo aluno: '))
a3 = str (input ('Terceiro aluno: '))
a4 = str (input ('Quarto aluno: '))
lista = [a1, a2, a3, a4]
escolhido = shuffle (lista)
print ('A ordem de apresentação será: ')
print (lista)

#MANIPULANDO STRINGS

frase = 'Curso em vídeo Python'
letras = frase [9]
print (letras)

frase = 'Curso em vídeo Python'
letras = frase [9:13]#vai imprimir até 12 (13-12)
print (letras)

frase = 'Curso em vídeo Python'
letras = frase [9:21]#vai imprimir até 20 (21-1)
print (letras)

frase = 'Curso em vídeo Python'
letras = frase [9:21:2]#vai imprimir até 20 (21-1), pilando de 2 em 2
print (letras)

frase = 'Curso em vídeo Python'
letras = frase [:5]# mesma coisa que [0:5]
print (letras)

frase = 'Curso em vídeo Python'
letras = frase [15:]# fatia do 15 até o final da string
print (letras)

frase = 'Curso em vídeo Python'
letras = frase [9::3]# ::começa do 9, vai até o final pulando de 3 em 3
print (letras)

#Testes aula 9-strigs
frase = 'Curso em vídeo Python'
print (frase)
print (frase[3])
print (frase[3:13])
print (frase[:13])
print (frase[3:])
print (frase[0:15])
print (frase[1:15:2])
print (frase[::2])
print (frase.count('o'))#conta quantas letras o há
print (frase.upper().count('O'))#transforma em maiúsculo e conta o maiúsculo
print (len(frase))#conta letras e espaços
print (frase.replace('Python', 'C++'))#substitui Python por C++
print ('Curso' in frase)
print (frase.find ('Curso'))# fornece posição da palavra
print (frase.lower().find ('python'))#transformou Python em mínúsculo antes de dar a posição
print (frase.split)

print ('''Os peixes são animais vertebrados, aquáticos, tipicamente ectotérmicos,
que possuem o corpo fusiforme, os membros transformados em barbatanas ou nadadeiras 
(ausentes em alguns grupos) sustentadas por raios ósseos ou cartilaginosos, 
guelras ou brânquias com que respiram o oxigénio dissolvido na água 
(embora os dipnóicos usem pulmões) e, na sua maior parte, o corpo coberto de escamas.''')
#comando para imprimir uma string longa

frase = 'Curso em vídeo Python'
dividido = frase.split()
print (dividido)#divide  a string
print (dividido[0])#divide e só mostra o elemento do índice
print (dividido [2][3])#[2] vídeo [3] letra do índice 3

#Desafio 22 - manipulando texto
nome = str(input('Digite seu nome completo: ')).strip() #retira espaços inúteis
print('Analisando seu nome:')
print('Seu nome em maiúsculo é {}.'.format (nome.upper()))
print('Seu nome em minúsculo é {}.'.format (nome.lower()))
print ('Seu nome tem ao todo {}.'.format (len(nome)-nome.count(' ')))#vc retira o espaços entre os nomes
#print ('Seu primeiro nome tem {} letras.'.format (nome.find (' ')))#ele diz a posiçaõ do primeiro espaço, que delimita o primeiro nome
separa = nome.split()
print ('Seu primeiro nome é {} e ele tem {} letras.'.format (separa [0], len (separa [0])))

#Desafio 23 Digitos separados de um número

#Só consigo analisar números com 4 algarismos
#num = int (input('Informe um número: '))
#n = str (num)#converte número em string
#print ('Analisando o número {}, podemos observar:'.format(n))
#print ('{} unidade(-s);'.format (n[3]))
#print ('{} dezena(-s);'.format (n[2]))
#print ('{} centena(-s);'.format (n[1]))
#print ('{} milhar(-es);'.format (n[0]))

#Consigo analisar qualquer número e não transformar em string
num = eval (input ('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print ('Analisando o número {}, podemos observar:'.format (num))
print ('{} unidade(-s);'.format (u))
print ('{} dezena(-s);'.format (d))
print ('{} centena(-s);'.format (c))
print ('{} milhar(-es);'.format (m))

#Desafio 24- faça um programa e diga se um nome começa ou não com santo
cidade = str (input ('Digite a cidade em que você nasceu: ')).strip()#retiro espaços desnecessárioxs
print (cidade[:5].upper() == 'SANTO')#comando upper padroniza, pois converter tudo em maiúsculo. Ou seja a pessoa pode escrever santo, SANTO, SAnto

#Desafio 25 procurar um astring dentro de outra
#um programa que verifica se existe a palavra silva
nome = str (input('Digite seu nome completo, sem abreviaturas: ')).strip()
print ('Seu nome tem Silva? {}.'.format ('Silva' in nome.upper()))

#Desafio 26 - primeira  e última letra de uma string
frase = str (input ('Digite uma frase: ')).strip ().upper()
print ('A letra A aparece {} vezes na frase.'.format (frase.count ('A')))
print ('A primeira letra A apareceu na posição {}.'. format (frase.find ('A')+1))#soma 1 para driblar a real posição que é zero
print ('A última letra A apareceu na posição {}.'. format (frase.rfind ('A')+1))#rfind procura do final para o começo

#Desafio 27-cortar string e dizer primeiro e ultimo nome
n = str (input ('Digite seu nome completo, sem abreviações: ')).strip()
nome = n.split()# a variável nome recebe o split 
print ('Prazer em conhecê-lo!')
print ('Seu primeiro nome é {}.'.format(nome[0]))
print ('Seu último nome é {}'.format(nome[len(nome)-1]))#escrever nome de qualquer comando

# Aula 10-estruturas condicionais (if e else)
#nome = str (input ('Digite seu nome: '))
#if nome == 'Gustavo':
    #print ('Que nome lindo você tem!')
#else:
    #print ('Seu nome é comum!')
#print ('Bom dia {}!'.format (nome))#esse print aparece para todos

nome = str (input ('Digite seu nome completo: ')).strip ().upper ()
n1 = float (input ('Digite a primeira nota: '))
n2 = float (input ('Digite a segunda nota: '))
média = (n1 + n2)/2
if média >= 6:
    print ('Sua média foi {} {}!. Parabéns!'. format (média, nome))
else:
    print ('{} sua média foi {} e está abaixo do esperado. Procure seu professor.'.format (nome,média))
    
print ('Independente da nota continuem estudando! Não desanimem!')

#Desafio 28-jogo da adivinhação
#import random
#n = int (input ('Escolha um número de 0 a 5: '))
#lista = [0,1,2,3,4,5]
#computador = random.choice (lista)
#lista = [0,1,2,3,4,5]
#print ('O computador pensou o número {}.'.format (computador))
#if n == computador:
    #print ('Parabéns você adivinhou !!!')
#else:
    #print ('Que pena, você errou !!!')
#print ('Se você errou tente novamente. Não desanime!')

#outra forma de fazer 
from random import randint
from time import sleep#faz o computador aguardar
computador = randint(0, 5)#faz o computador escolher
print ('*'*55)
print ('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print ('*'*55)
jogador = int (input ('Que número eu pensei? '))#jogador tenta adivinhar
print ('Processando...')
sleep (3)#espera 3 segundos para processar
if computador == jogador:
    print ('Parabéns! Você conseguiu me vencer')
else:
    print ('Eu ganhei! Eu pensei no número {} e não no número {}.'.format (computador, jogador))
    
    
#Desafio 29-radar de velocidade
velocidade = float (input ('Velocidade registrada pelo radar, em km/h, foi de: '))

if velocidade > 80.0:
    excesso = velocidade - 80.0
    multa = excesso* 7# 7 reais por km excedido da velocidade
    print ('Você foi multado em {}, pois você excedeu em {} km/h a velocidade máxima de 80 km/h.'.format (multa, excesso))
else:
    print ('Parabéns! Você respeitou o limite de velocidade de 80 km/h.') 
    
 
#Desafio 30-número par ou impar
 #n = int (input ('Escolha um número: '))
#if n % 2 == 0:
    #print ('O número {} é PAR.'.format (n))
#else:
    #print ('O número é ÍMPAR.'.format (n))
    

n = int (input ('Escolha um número: '))
if n % 2 != 0:# != diferente
    print ('O número {} é IMPAR.'.format (n))
else:
    print ('O número é PAR.'.format (n)) 

 #Desafio 30-preço da passagem
#distância = float (input ('Qual é a distância até o seu destino, em Km? '))
#if distância <= 200:
    #p = distância * 0.5
    #print ('Para distância de {} Km o preço da passagem será R$ {:.2f}'. format (distância, p))
#else:
    #pd = distância * 0.45
    #print ('Para distância de {} Km o preço da passagem será R$ {:.2f}'. format (distância, pd))
        
#Outra forma       
distância = float (input ('Qual é a distância até o seu destino, em Km? '))
p = distância * 0.5 if distância <=200 else distância * 0.45 
print ('O preço da passagem será de R$ {:.2f}.'.format (p))


#Desafio 33-maior e menor valor

n1 = int (input ('Digite o primeiro número: '))
n2 = int (input ('Digite o segundo número:  '))
n3 = int (input ('Digite o terceiro número: '))
#verificando quem é menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
#verificando que é o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print ('O menor valor digitado é {} e o maior é {}.'.format (menor, maior))

#Desafio 34-aumentos múltiplos
sal = float (input ('Digite o valor do seu salário: R$'))
if sal <= 1250:
    novosal = (sal + (sal * 0.15))
print ('Você teve um aumento de 15%, e seu novo salário é de R${:.2f}.'.format (novosal))

else:
    novosal = (sal + (sal * 0.10))
print ('Você teve um aumento de 10%, e seu novo salário é de R$ {:2f}.'.format (novosal))


#Desafio 35-verificar se é possível formar um triângulo
print ('#' * 24)
print ('Analisador de triângulos')
print ('#' * 24)
a = float (input ('Valor do primeiro segmento: '))
b = float (input ('Valor do segundo segmento:  '))
c = float (input ('Valor do terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print ('Os segmentos {}, {} e {} FORMAM um triângulo.'.format (a, b, c))
else:
    print ('Os segmentos {}, {} e {} NÃO FORMAM um triângulo.'.format (a, b, c))
   
#AULA 11-colocar cor e estilo nas letras
 #print ('\033[4;30;45m Olá mundo!\033[m')
#print ('\033[1;31m Olá mundo!\033[m')
#print ('\033[1;30;37m Olá mundo!\033[m')

nome = 'André'
print ('Prazer em conhecê-lo {}{}{}!'.format ('\033[1;31;33m', nome,'\033[m'))
