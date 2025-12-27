#Aula 16-TUPLAS símbolo ()
#AS TUPLAS SÃO IMUTAVEIS#

'''lanche = ('hambúrger','suco','pizza','pudim') #pode ser sem parênteses
print(lanche)
print(lanche[1])
print(lanche[-4])
print(lanche[1:3])#retira o elemento 3
print(lanche[2:])
print(lanche[:2])#mostra o elemento 0 e 1 e retira o 2

for comida in lanche:
    print ('Eu vou comer {}.'.format(comida))#print(f'Eu vou comer {comida}'')
print('Comi pra caramba!')

for cont in range (0, len(lanche)):
    print (lanche[cont])#se colocar só o cont imprimi os números
print('Comi pra caramba!')

#PARA MOSTRAR A POSIÇÃO

for pos, comida in enumerate (lanche):
    print ('Eu vou comer {} na posição {}.'.format(comida, pos))
    
lanche = ('hambúrger','suco','pizza','pudim')
print (sorted(lanche)) # ordena a tupla'''
    
a = (2,5,4)
b = (5,8,1,2)
c = (a + b)
print(c)
print(len(c))#conta o numero de elementos
print(c.count(5))#quantas x aparece 5 na tupla c
print(c.index(8))#mostra a posiçao do elemento


#Desafio 94-Unindo dicionários e listas
galera = list()
pessoa = dict()
soma = media = 0

while True:
    pessoa.clear()#esvazia a lista para receber outros dados
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper() [0]#pega só a primeira letra
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy()) # acrescenta os nomes na lista
    
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper() [0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
 
print('-=' * 30)   
print('A) Ao todo temos {} pessoas cadastradas.'.format(len(galera)))
media = soma / len(galera)
print('B) A média das idades é de {:.2f} anos.'.format(media))
print('C) As mulheres cadastradas foram ', end = ' ')
for p in galera:
    if p['sexo'] in 'Ff':
        print('{}'.format(p['sexo'], end = ' '))
print('D) lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('                ')
        for k, v in p.items():
            print ('{} = {}'.format(k, v), end = ' ')
            print()
print('<< ENCERRADO >>')
        

#del (c) esse comando apaga a tupla toda


#Desafio 72-número por extenso
cont = ('zero', 'um','dois','três','quatro',
'cinco', 'seis','sete','oito','nove',
'dez','onze','doze','treze','catorze',
'quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    núm = int(input('Digite um número entre 0 e 20: '))
    if 0 <= núm <= 20:
        break
    print ('Tente novamente.', end= '')#end = '' não pular linha
    
print ('Você digitou o número {}.'.format (cont[núm]))
#print (f'Você digitou o número {cont[núm]})


#Desafio 73-Tuplas com times
times = ('Atlético-MG','Palmeiras','Fortaleza','RB Bragantino','Flamengo','Athletico-PR',	
'Ceará','Santos','Atlético-GO','Bahia','Internacional','Corinthians','Fluminense',
'Juventude','Sport','São Paulo','América-MG','Cuiabá','Grêmio','Chapecoense')

print('=-='*39)
print ('Lista de times do Brasileirão: {}.'.format(times))
print('=-='*39)
 
print ('Os 5 primeiros colocados são: {}.'.format(times[0:5]))
print ('=-='*20)
print ('Os últimos 4 colocados são: {}.'.format(times[16:20]))# ou [-4:0]
print ('=-='*20)
print ('Os times em orde alfabética são: {}.'.format(sorted(times)))
print ('=-='*11)
print ('O Chapecoense está na {}ª posição.'. format(times.index('Chapecoense') + 1))#index para encontrar um termo + 1 posiçao real
#print(f'O Chapecoense está na {times.index("Chapecoense")+ 1}ª posição')
print ('=-='*11)


#Desafio 74-maior e menor número em tuplas
from random import randint
sorteados = (randint(1,10), randint(1,10), randint(1,10),randint(1,10), randint(1,10))#gera tupla
print ('Os valores sorteados foram: ', end = '')
for n in sorteados:#imprimi os valor fora da tupla
    print ('{} '.format (n), end = '')
    
print ('\nO maior valor sorteado foi {}.'.format (max(sorteados)))#max método para tupla \n pula linha
print ('O menor valor sorteado foi {}.'.format (min(sorteados)))


#Desafio 75-análise de tupla
núm = (int(input('Digite um número: ')), 
int(input('Digite outro número: ')),
int (input('Digite mais um número: ')),
int (input ('Digite o último número: ')))

print ('Você digitou os números {}.'.format (núm))
print ('O valor 9 apareceu {} vezes.'.format (núm.count (9)))
if 3 in núm:
    print ('O valor 3 apareceu na {}ª posição.'.format (núm.index(3) + 1))
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print ('Os valores pares digitados foram ' , end = '')
for n in núm:
    if n % 2 == 0:
        print (n, end = '')
        
        
#Exercício 76-lista de preços com tuplas
print('=' * 40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))  # comando para centralizar
print('=' * 40)

listagem = ('Lápis', '1.75',
            'Borracha', '2.00',
            'Caderno', '15.90',
            'Estojo', '25.00',
            'Transferidor', '4.20',
            'Compasso', '9.99',
            'Mochila', '120.32',
            'Canetas', '22.30',
            'Livro', '34.90')
for posição in range (0, len(listagem)):
    if posição % 2 == 0: #observe que os produtos estão na posição par
        print(f'{listagem[posição]:.<30}', end='')#alinhado a esquerda com pontos não pular linha com o preço
    else:
        print(f'R${listagem[posição]:>7}')
print('=' * 40)

#Desafio 77-contar vogal na tupla
palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM'
'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 
'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for p in palavras:
    print ('\nNa palavra {} temos '.format (p), end = '')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print (letra, end = '')
            
            
AULA 17-LISTAS

#num = (2,5,9,1)#tupla
#num [2] = 3
#print (num)

#num = [2,9,5,1,9]
#num [2] = 0#mudou o elemento da posição 2
#num.append (7)#estou adicionando o valor 100
#num.sort ()#ordena
#num.sort (reverse=True)#ordena reverso
#print(num)
#num.insert (2,1000)#inseri o valor 1000 na posição 2
#num.pop()#deleta o último valor
#num.remove (9)#remove um valor numérico em sua primeira ocorrência
#if 100 in num:#consulta se o número está na lista
    num.remove (100)
else:
     print ('O número não existe na lista.')
    
#print (num)
print ('Essa lista tem {} elementos.'.format(len (num)))
#print (f'Essa lista tem {len(num)} elementos.')

#valores = list()
#valores.append (1)
#valores.append (1000)
#valores.append (3)

#for v in valores:
    #print (f' {} ...', end = '')#não pula linha
    #print ('{} ...'.format(v), end = '')
    
#for c, v in enumerate (valores):
    #print ('Na posição {} encontrei o valor {}.'.format (c,v))
#print ('Cheguei ao final da lista.')

#valores = list()
#for cont in range (0, 5):#incluir valores na lista
    #valores.append (int(input('Digite um valor: ')))
#print ('A lista de números é: {}.'.format (valores))

a = [1, 23, 12, 100]
#b = a # as duas listas estão ligadas
b = a[:] #b recebe todos os elementos de a, isso é uma COPIA
b [2] = 8
print ('Lista A: {}.'.format(a))
print ('Lista B: {}.'.format (b))


#Desafio 78-maior e menor valor em lista
listnum = []
maior = 0
menor = 0
for c in range(0, 5):
    listnum.append(int(input('Digite um valor para a posição {}: '.format(c)))),
    if c == 0:
        maior = menor = listnum[c]#vc digitou um número somente ele é o maior e o menor
    else:
        if listnum[c] > maior:
            maior = listnum[c]
        if listnum[c] < menor:
            menor = listnum[c]

print('=-' * 30)
print(f'Você digitou os valores {listnum}')
print(f'O maior valor foi {maior}, nas posições .', end='')
for i, v in enumerate(listnum):
    if v == maior:
        print(f'{i}...', end='')
print ()
print(f'O menor valor foi {menor}, nas posições .', end='')
for i, v in enumerate(listnum):
    if v == menor:
        print(f'{i}...', end='')
print()


# Desafio 79-valores únicos em uma lista

números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Adicionado com sucesso!')
    else:
        print('Valor duplicado! Não será adicionado.')

    resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if resposta in 'N':
        break
    print('Digite novamente sua opção')
print('=-' * 30)
números.sort()
print('Você digitou os valores {}.'.format(números))
print('=-' * 30)


#Desafio 80: lista ordenada sem repetições
lista = []
for c in range (0,5):
    n = int(input('Digite um número: '))
    if c == 0 or c > lista[-1]:#primeiro valor e último valor
        lista.append(n)
        print ('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                print ('Adicionado na posição pós {} da lista...'.format(pos))
                break
            pos += 1
print('-=' * 30)
print ('Os valores digitados, em ordem, foram {}'.format (lista))



#Desafio 81-Extraindo dados de uma lista
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    resposta = str(input('Quer continuar?[S/N]: ')).upper().strip()
    if resposta in 'N':
        break
print('=-' * 30)
print('Você digitou {} números.'.format(len(lista)))
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}.')
if 5 in lista:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')
    
    
#Desafio 82-dividindo valores em várias listas
num = list()
pares = list()
ímpares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N]: ')) .upper()
    if resp in 'N':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        ímpares.append(v)
print('*=' * 30)
print(f'A lista dos valores digitados foi {num}.')
print(f'A lista dos valores pares foi {pares}.')
print(f'A lista dos valores ímpares foi {ímpares}.')
print('*=' * 30)


#Desafio 83-validando expressões matemáticas

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len (pilha) > 0:
            pilha.pop()
        else:
            pilha.append (')')
            break
if len (pilha) == 0:
    print ('Sua expressão é válida!')
else:
    print ('Sua expressão está errada!')
    
    
    
#AULA 18-LISTAS 

'''pessoas = [['André', 45],['Letícia', 8], ['Enrico', 5]]
print(pessoas[0][0])#André
print(pessoas[0][1])
print(pessoas[2][1])
print(pessoas[2])

teste = []
teste.append('André')
teste.append(40)
galera = []
galera.append(teste[:])
#galera.append(teste)se deixar assim ele repetirá a lista [['Maria', 22], ['Maria', 22]]
teste[0] = 'Maria'
teste[1] = 22
#galera.append(teste)
galera.append(teste[:])
print(teste)
print(galera)'''

'''galera = [['Gustavo', 11], ['André', 45], ['Lúcia', 23], ['Geni', 70]]
print(galera[0])
print(galera[0][0])
print(galera[3][1])
print (galera[2][1])

for p in galera:
    print(p)#printa sub-listas
    print(p[0])#só nomes
    print(p[1])#só idades
    print ('{} tem {} anos de idade.'.format(p[0],p[1]))
    #print (f'{p[0]} tem {p[1]} anos de idade} anos de idade.')'''
    
galera = list()
dado = list()
totmaior = totmenor = 0
for c in range (0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()#apagar os dados da lista dados
    
#print(galera)

for p in galera:
    if p[1] >= 21:
        print('{} é maior de idade.'.format(p[0]))
        totmaior += 1
    else:
        print('{} é menor de idade.'.format(p[0]))
        totmenor += 1
      
print ('Temos {} pessoas maiores e {} menores de idade.'.format(totmaior, totmenor))

#Desafio 84-lista composta e análise de dados
temp = []
princ = []
maior = menor = 0

while True:
    temp.append(str(input('Nome: ')))#p[0]
    temp.append(float(input('Peso: ')))#p[1]
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar?[S/N]')).upper().strip()
    if resp in 'N':
        break
print('=-' * 30)
print('Ao todo você cadastrou {} pessoas.'.format(len(princ)))#len dispensa contador
print(f'O maior peso foi de {maior} Kg. Peso de', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(F'O menor peso foi de {menor} Kg. Peso de', end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
        
        
#Exercício 85-lista com pares e ímpares
núm = [[],[]]
valor = 0
for c in range (0,7):
    c += 1
    valor = int(input('Digite número {}º valor: '.format(c)))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
        
print('=-' * 40)
#print('Todos os valores são {}.'.format(núm))
núm[0].sort()#ordena os pares
núm[1].sort()#ordena os ímpares
print('Os valores pares digitados foram {}.'.format(núm[0]))
print('Os valores ímpares digitados foram {}'.format(núm[1]))

  
# Desafio 86-criar matriz

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input('Digite um valor para {}, {}: '.format(l, c)))
print('=*' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()


#Desafio 87-calculos em matrizes

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input('Digite um valor para {}, {}: '.format(l, c)))
print('=*' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 ==0:
            spar += matriz[l][c]
    print()
print('=*' * 30)
print(f'A soma dos valores pares é {spar}.')
for l in range(0,3): #soma da terceira coluna e a linha é fica-segunda linha
    scol += matriz [l][2]
print(f'A soma dos elementos da terceira coluna é {scol}.')

for c in range(0,3):
    if c == 0:
        mai = matriz[l][c]
    elif matriz[l][c] > mai:
        mai = matriz[l][c]

print(f'O maior elemento da lista é o {mai}.')

# Desafio 88-palpites para a Mega Sena:
from random import randint
lista = []
jogos = []
print('-=' * 30)
print('          JOGA NA MEGA SENA           ')
print('-=' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
            if cont >= 6:
                break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')

    
 #Desafio 89-listas compostas   
ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nome: '))
    nota2 = float(input('Nome: '))
    media = nota1 + nota2 / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar: [S/N]: ')).upper
    if resp in 'N':
        break
print('-=' * 30)
print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
print('-=' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int (input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha)-1:
        print(f'Notas de {ficha[opc][0]} são {cad[opc][1]}')
print('<<<VOLTE SEMPRE>>>')  
    
#AULA 19-DICIONÁRIO

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
#pessoas ['peso'] = 97.8 adiciona peso
#pessoas['nome']='Leandro' troca nome
print(pessoas)
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')#aspas duplas para não dar erro
print(pessoas.keys())
print(pessoas.items())
pessoas['nome']='Leandro'
#del pessoas['sexo'] apaga sexo
for k, v in pessoas.items():
    print(f'{k}={v}')

#criando dicionário em uma lista
brasil = []
estado1 = {'uf': 'Rio de Janeiro','sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)

estado = dict()
brasil = []
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: ')).upper()
    brasil.append(estado.copy())#tem de botar o copy()
print(brasil)
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
    
                     
#Desafio 90-Dicionário em Python
aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input('Média de {}: '.format(aluno['nome'])))
if aluno['média']>= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno ['média'] <7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=' * 30)
    
for k, v in aluno.items():
    print(f'  -{k} é igual a {v})
          

#Desafio 91-Jogo de dados
from random import randint
from time import sleep
from operator import itemgetter
ranking = dict() #armazenará os valores e ordem. Está vazio.
jogo = {'jogador 1':randint(1,6),
'jogador 2':randint(1,6),
'jogador 3':randint(1,6),
'jogador 4':randint(1,6)}
print(jogo)
print('Valores sorteados: ')
for k, v in jogo.items():
    print('O {} tirou {} no dado.'.format(k,v))
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1),reverse=True)# parte 1 é a do randint
#print(ranking)#mostra em forma de lista
print('=' * 27)
print(  '==RANKING DOS JOGADORES==')
for i, v in enumerate (ranking):#transforma lista em dicionario
    print('{}º lugar: {} com {}.'.format(i+1,v[0],v[1]))
    sleep(1)
print('=' * 27)


 #Desafio 92-cadastro de trabalhador
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não possui): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k,v in dados.items():
    print(f'{k} tem o valor {v}')
          
          
#Desafio 93-cadastro de jogador de futebol
jogador = dict()
partidas = []
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
for c in range (0, tot):
  partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('=-'*30)
print(jogador)
for k, v in jogador.items():
  print(f'O campo {k} tem o valor {v}')
  print('=-'*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador["gols"]):
  print(f
        '    => Na partida {i}, fez {v} gols.')
print(f' Foi um total de {jogador["total"]} gols.')

          
          
#Desafio 94-Unindo dicionários e listas
galera = list()
pessoa = dict()
soma = media = 0

while True:
    pessoa.clear()#esvazia a lista para receber outros dados
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper() [0]#pega só a primeira letra
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy()) # acrescenta os nomes na lista
    
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper() [0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
 
print('-=' * 30)   
print('A) Ao todo temos {} pessoas cadastradas.'.format(len(galera)))
media = soma / len(galera)
print('B) A média das idades é de {:.2f} anos.'.format(media))
print('C) As mulheres cadastradas foram ', end = ' ')
for p in galera:
    if p['sexo'] in 'Ff':
        print('{}'.format(p['sexo'], end = ' '))
print('D) lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('                ')
        for k, v in p.items():
            print ('{} = {}'.format(k, v), end = ' ')
            print()
print('<< ENCERRADO >>')
          
 
#Desafio 95-aprimoramento do 93 para mais jogadores
time = list()
jogador = dict()
partidas = []

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N. ')
    if resp == 'N':
        break

print('=-'*30)#cabeçalho
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)

for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
        print()
print('=-'*40)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]["nome"]):
            print(f'          No jogo {i+1} fez {g} gols. ')
print('-'*40)
print('Volte sempre')
        

 #Aula 20-Funções

'''def lin():#não executa
    print('-+' * 30)

#programa principal
lin()
print('SISTEMA DE ALUNOS')
lin()
print('CADASTRO DE FUNCIONÁRIOS')
lin()
print('ERRO DO SISTEMA')

def título (txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)

#programa principal para
título('     CURSO EM VÍDEO     ')
título('     APRENDA PYTHON     ')
título('     GUSTAVO GUANABARA  ')'''

'''a = 4
b = 5
s = a + b
print(s)
a = 8
b = 9
s = a + b
print(s)
a = 2
b = 1
s = a + b
print(s)

def soma (a, b):
    print(f' A = {a} e B = {b}')
    soma = (a + b)
    print(f' A soma A + B = {soma}')

#programa principal
soma(4,5)
soma(2,9)
soma(2,1)

def contador(* núm):
    print(núm)
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todos {tam} valores')
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

def dobra(lst):
    pos = 0 #variável
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
# programa principal
valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)'''


def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}.')

soma(5, 2)
soma(2, 9, 4)
          
          
          
 #Desafio 96-cálculo de área
def área (l, c):
    a = l * c
    print(f'A área de um terreno de {l} x {c} é de {a} m2.')


print('Controle de terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)


#Desafio 97-print especial
def escreva (msg):
    tam = len(msg) + 4 # dar 4 = antes de começar a escrever
    print('=' * tam)
    print(f'  {msg}  ')#centralizar a mensagem
    print('=' * tam)

escreva('oi')


#Desafio 98-função de contador
from time import sleep
def contador (i, f, p): #inicio, fim e passou
    print('=' * 31)
    print(f'Contagem de {i} até {f} de {p} em {p}:.')
    sleep(2.5)

    if p < 0:
        p *= -1 #deixa o passo positivo
    if p == 0: #contorna o passo ser igual a 0
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f' {cont} ', end=' ', flush=True)#flush é para aparecer os numeros aos poucos
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'  {cont} ', end=' ', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')
    print('=' * 31)

#programa principal
contador (0, 10, 1)
contador (10, 0, 2)
print('=' * 31)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))

contador(ini, fim, pas)
          

#Desafio 99-função que descobre o maior
from time import sleep
def maior(*num):
    cont = maior = 0
    print('=' * 33)
    print("Analisando os valores passados...")
    for valor in num:
        print(f'{valor} ', end=' ', flush=True)
        sleep(0.4)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


#programa principal
maior(2,9,4,5,7,1)
maior(2,0)

#Aula 21-funções
#docstring: aspas duplas três vezes
def contador (i,f,p):
    """
    faz uma contagem e mostra na tela
    :param i: início
    :param f: final
    :param p: passo
    :return: sem retorno
    """
    c=i
    while c<=f:
        print(f'{c}', end='..')
        c+=p
    print('FIM!')

contador (2,10,2)
help (contador)


#parâmetros opcionais
def somar (a=0,b=0,c=0):#se não declarar o a,b, c ele receberá zero
    s = a+b+c
    print(f'A soma vale {s}.')
somar (3,2,5)
somar(8,4) #aqui c vale zero

#escopo de variáveis
def teste():
    global n #usa o valor global sempre
    x = 8
    n = 1
    print (f'Na função teste n vale {n}.')
    print(f'Na função teste n vale {x}.')


#programa principal
n = 100 #está dentro do escopo global0
print (f'No programa principal n vale {n}.')


#comando return
def somar (a=0,b=0, c=0):
    s = a + b + c
    return s
r1 = somar (3,2,5)
r2 = somar (1,2)
r3 = somar (1000)

print (f'Meus cálculo deram {r1}, {r2} e {r3}')
          

#Aula 23-tratamento de exceções
try:
    n = int(input('Digite o numerador: '))
    d = int(input('Digite o denominador: '))
    r = n / d
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou!')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar dados.')
except Exception as erro:
    print('O erro econtrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')
          

#Desafio 100-funções para sortear e somar
from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range (0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print (f'Somando os valores de {lista} temos {soma}.')


números = list()
sorteia(números)
somaPar(números)
          
          
#Desafio 101-funções para votação
def voto (ano):
    from datetime import date #economiza memoria e só usa dentro
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'

#Programa principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(1976))
          
          
# Desafio 102-função para fatorial

def fatorial(n, show=False):  # não mostra o cálculo
    """
    -> Calcula o fatorial de um número.
    :param n: o número a ser calculado.
    :param show:(opcional) mostrar ou não o cálculo.
    :return: o fatorial de um número n.
    """

    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

# programa principal
print(12 * '+-')
print(fatorial(5, show=True))  # aparece o cálculo
print(12 * '+-')
print(fatorial(5, show=False))  # não aparece o cálculo
print(12 * '+-')

help(fatorial)
          
          
# Desafio 103-ficha do jogador
def ficha (jog='<desconhecido>', gol=0): #se eu não digitar nada imprimirá esses parâmetros
    print (f'O jogador {jog} fez {g} gol(-s) no campeonato.')

# programa principal
n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int (g)
else:
    g = 0
if n.strip() == '':
    ficha (gol = g)
else:
    ficha(n, g)

          
          
# Desafio 104-validando entrada de dados
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO: Digite um número válido.\033[m')#fonte vermelha
        if ok:
            break
    return valor

# programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
          
          
# Desafio 105-Analisando e gerando dicionários
def notas (*n, sit=False):
    '''
    ->função para analisar notas e faltas de vários alunos
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: opcional, caso queira mostrar situaçao coloque site=True
    :return: retorna dicionário com as informações sobre cada aluno
    '''
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


# programa principal
resp = notas (5.5, 2.5, 9.0, 8.5, sit=True)#site=True aparece situação
print (resp)

       
          
 # Desafio 106-sistema de ajuda interativo em Python.
from time import sleep
c = ('\033[m',            #0-sem cor
     '\033[0; 30; 41m',   #1-vermelho
     '\033[0; 30; 42m',  #2-verde
     '\033[0; 30; 43m',  #3-amarelo
     '\033[0; 30; 44m',  #4-azul
     '\033[0; 30; 45m',  #5-roxo
     '\033[7; 30m'        #6-branco
     );


def ajuda (com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help (com)
    print(c[0], end='')
    sleep(2)


def título (msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f' {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)

#programa principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando) # ajuda é um comando
título('ATÉ LOGO!', 1)

