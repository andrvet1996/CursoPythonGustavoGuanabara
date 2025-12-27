#Aula 12-condições aninhadas
nome = str (input ('Qual é o seu nome: '))
if nome == 'Gustavo':
    print ('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print ('Seu nome é bem popular no Brasil!')
elif nome in ('Ana Cláudia Jéssica Julina'):
    print ('Belo nome feminino!')
else:# se vc tirar o else funciona,mas só printa o último print
    print ('Seu nome é bem normal!')
print ('Tenha um bom dia, {}!'.format (nome)) 

#Desafio 36-número de prestações não pode exceder 30% do salário
v = float (input ('Qual o valor da casa que deseja adquirir? R$'))
s = float (input ('Qual é o seu salário? R$'))
t = int (input ('Em quantos anos de financiamento?' ))
valprest = (v / (t * 12))#parcelas mensais
lim30 = (0.3 * s)
if valprest <= lim30:
    print ('O empréstimo para adquirir uma casa de {:.2f}, a ser pago em {} parcelas mensais, no valor de R$ {:.2f} foi APROVADO!'.format (v, t, valprest))
else:
    print ('O empréstimo NÃO FOI APROVADO, pois o valor da prestação ultrapassa 30% de sua renda mensal.')
    
Dsafio 37- conversor de decimal para binário, octal e hexadecimal    
num = int (input ('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[1] converter para BINÁRIO 
[2] converter para OCTAL 
[3] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}.'.format (num, bin(num)[2:]))#[2;0] retira algarismos desnecessários
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}.'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida! Tente novamente.')
    
    
#Desafio 38-comparara 2 números e dizer maior, menor ou =

n1 = int (input ('Digite o primeiro número: '))
n2 = int (input ('Digite o segundo número:  '))
if n1 > n2:
    print ('O número {} é MAIOR que {}.'.format (n1, n2))
elif n1 < n2: 
    print ('O número {} é MENOR que {}.'.format (n1, n2))
else:
    print ('Os números são IGUAIS.')
    
#Desafio 39-alistamento militar
    
ano_atual = int(input('Digite o ano atual: '))
ano_nascimento = int(input("Digite seu ano de nascimento: "))
idade = ano_atual - ano_nascimento
ano_para_se_alistar = ano_atual + (18 - idade)
if idade == 18:
    print('Você deve se alistar esse ano. Procure a Junta Militar mais próxima de sua residência.'.upper())
elif idade < 18:
    print('Você deve se alistar em {}.'.format(ano_para_se_alistar).upper())
else:
    print('Você precisa se alistar IMEDIATAMENTE. Procure a Junta Militar mais próxima de sua residência.'
          
  #outra forma de fazer      
from datetime import date #não precisa digitar o ano atual
atual = date.today().year
nasc = int (input ('Ano de nascimento: '))
idade = atual - nasc
print ('Quem nasceu em {} tem {} anos em {}.'.format (nasc,idade,atual))
if idade == 18:
    print ('Você tem de se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade 
    print ('Ainda faltam {} anos para o alistamento.'.format (saldo))
    ano = saldo + atual
    print ('Seu alistamento será em {}.'.format (ano))
else:
    saldo = idade - 18 # posso chamar de saldo porque está dentro da identação
    print ('Você já deveria ter se alistado há {} anos.'.format (saldo))
    ano = atual - saldo# posso dar o memso nome devido a identação
    print ('Você deveria ter se alistado em {}.'.format (ano))
          
          
   #Desafio 30-cálculo média
#n1 = float (input ('Digite a primeira nota: '))
#n2 = float (input ('Digite a segunda nota:  ')) 
#média =  (n1 + n2) / 2
#if média < 5.0:
    #print ('Você foi REPROVADO, pois a média {:.1f} é menor que 5.0.'.format (média))
#elif média > 7.0:
    #print ('Você foi APROVADO, pois a média {:.1f} é maior que 7.0. Parabéns!'.format (média))
#else:
    #print ('Você está em RECUPERAÇÃO, pois a média {:.1f} está entre 5.0 e 6.9.'.format (média))
    
#outra forma
n1 = float (input ('Digite a primeira nota: '))
n2 = float (input ('Digite a segunda nota:  ')) 
média =  (n1 + n2) / 2
if média < 5.0:
    print ('Você foi REPROVADO, pois a média {:.1f} é menor que 5.0.'.format (média))
elif média >=5.0 and média <7.0:
    print ('Você está em RECUPERAÇÃO, pois a média {:.1f} está entre 5.0 e 6.9.'.format (média))
else:
    print ('Você está APROVADO, pois a média {:.1f} é maior que 7.0. Parabéns!!!'.format (média))
          
          
 #Desafio 41-categoria de atletas
from datetime import date
data_atual = date.today().year
nome = str (input ('Nome completo do atleta: '))
dn = int (input ('Ano de nascimento: '))
idade = data_atual - dn
if idade <= 9:
    print ('O atleta {} tem {} anos e pertence a categoria MIRIM.'.format (nome,idade))
elif 9< idade <=14:
    print ('O atleta {} tem {} anos e pertence a categoria INFANTIL.'.format (nome,idade))
elif 15< idade <=19:
    print ('O atleta {} tem {} anos e pertence a categoria JUNIOR.'.format (nome,idade))
elif 20< idade <=25:
    print ('O atleta {} tem {} anos e pertence a categoria SÊNIOR.'.format (nome,idade))
else:
    print ('O atleta {} tem {} anos e pertence a categoria MASTER.'.format (nome,idade))
          
          
#Desafio 42-analisador de triângulo
print('#' * 24)
print('Analisador de triângulos')
print('#' * 24)
a: float = float(input('Valor do primeiro segmento: '))
b = float(input('Valor do segundo segmento:  '))
c = float(input('Valor do terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos {}, {} e {} FORMAM UM TRIÂNGULO.'.format(a, b, c))
    if a == b == c:#não coloque elif,pois há duas possibilidades é ou não é triângulo
        #esse if está identado desse jeito porque está ligado ao tipo de triângulo
        print('O triângulo é EQUILÁTERO.')
    elif a != b and b != c and c != a:
        print('O triângulo é ESCALENO.')
    else:
        print('O triângulo é ISÓSCELES.')
else:
    print('Os segmentos {}, {} e {} NÃO FORMAM UM TRIÂNGULO')
          
#Desafio 43-IMC
peso = float (input ('Digite o seu peso (Kg): '))
alt = float (input ('Digite sua altura (m): '))
imc = peso / (alt**2)
if imc < 18.5:
    print ('Seu IMC é {:.1f}. Você está ABAIXO DO PESO IDEAL.'.format (imc))
elif 18.5 <= imc < 25.0:
    print ('Seu IMC é {:.1f}. O seu peso está NORMAL.'.format (imc))
elif 25.0 <= imc <  30.0:
    print ('Seu IMC é {:.1f}. Você está com SOBREPESO.'.format (imc))
elif 30.0 <= imc < 40.0:
    print ('Seu IMC é {:.1f}. Você está OBESO.'.format (imc))
else:
    print ('Seu IMC é {:.1f}. Você está com OBESIDADE MÓRBIDA.'.format (imc))
          
#Desafio 43-Descontos na loja
print('=' * 13)
print('LOJA DO ANDRÉ')
print('=' * 13)
preço = float(input('Preço das compras: R$ '))
print('''Condições de pagamento:
[1] à vista dinheiro/cheque 
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
condição = int(input('Escolha a forma de pagamento: '))
if condição == 1:
    desc = preço - (0.1 * preço)
    print('O valor a pagar, com o desconto de 10%, é de R${:.2f}.'.format(desc))
elif condição == 2:
    desc = preço - (0.05 * preço)
    print('O valor a pagar, com o desconto de 5%, é de R${:.2f}.'.format(desc))
elif condição == 3:
    parcela = preço / 2
    print('O valor a pagar, sem desconto, é de R${:.2f}, dividido em duas parcelas de R${:.2f}.'.format(preço, parcela))
elif condição == 4:
    acresc = preço + (0.20 * preço)
    parcelas = int(input('Número de parcelas: '))
    cada_parcela = acresc / parcelas
    print('O valor a pagar, com acréscimo de 20%, é de R${:.2f}, dividido em {} de R${:.2f}.'.format(acresc, parcelas, cada_parcela))
else:
    print('Opção \033[1;31mINVÁLIDA!\033[m Tente novamente.')#letra vermelha
    
          
  #Aula 13-LAÇOS DE REPETIÇÃO
#for c in  range (0, 6):#repete oi 6x
    #print ('Oi!')
#print ('FIM!')

#contagem
#for c in range (1, 6):#conta mas não imprimi o último número
    #print (c)
#print ('FIM!')

'''#contagem para trás
for c in range (0, 6, -1): 
    print (c)#acrescenta -1 para contar para trás
print ('FIM!')

#contagem pulando
for c in range (0, 6, 2): 
    print (c)#conta e pula de 2 em 2
print ('FIM!')'''

#n = int (input ('Digite um número: '))
#for c in range (0, n):#usuário define a contagem, mas não conta o último
    #print (c)
#print ('FIM!')

#n = int (input ('Digite um número: '))
#for c in range (0, n+1):#usuário define a contagem, conta o último n+1
    #print (c)
#print ('FIM!')

#i = int (input ('Início: '))#define início (i), contagem total (f+1) e pulos (p)
#f = int (input ('Fim:    '))
#p = int (input ('Passo:  '))
#for c in range (i, f+1, p):
    #print (c)
#print ('FIM!')

#for c in range (0, 4):
    #n = int (input ('Digite um número: '))# repetir o input n vezes
#print ('FIM')

soma = 0
for c in range (0, 4):
    n = int (input ('Digite um valor: '))
    soma += n # soma += n é o mesmo que soma = soma + n
print ('O somatório de todos os números digitados é {}.'.format (soma))
          
          
#Desafio 46-contagem regressiva
from time import sleep
for c in range (10, -1, -1):# o primeiro -1 faz a contagem chegar a zer
    print (c)
    sleep (0.5)#espera 1s entre os números
sleep (1)#espera 1s até o BUM
print ('BUM! BUM! BUM!')
          

 #Desafio 47-contagem dos números pares entre 0 e 50
#for n in range (1, 51):#imprimi de 1 a 50
    #if n % 2 == 0:
        #print (n, end=' ')#end = dá um espaço entre os números   
#outra forma    
for n in range (2, 51, 2):#imprimi de 1 a 50
        print (n, end=' ')#end = dá um espaço entre os números
  
          
 #Desafio 48-Soma ímpares múltiplos de três entre 1 e 500
soma = 0
cont = 0#contador
for n in range (1, 501, 2):
    if n % 3 == 0:
        cont = cont + 1# me diz quantos múltiplos de 3 há entre 1 e 500
        soma += n # = soma = soma + n
print ('A soma dos {} números múltiplos de 3, entre 1 e 500, é {}.'.format (cont, soma))
# o print não identa, pois vc precisa fazer todas as somas até o 500
                
#Desafio 49-tabuada
num = int (input ('Digite um número para ver sua tabuada: '))
print ('=' * 12)
for c in range (1, 11):#evita fazer 10 linhas
    print ('{} x {:2} = {}'.format (num, c, num*c))
print ('=' * 12)

 
#Desafio 50-soma de seis números pares
soma = 0
cont = 0
for n in range (1, 7):
    n = int (input ('Digite o valor {}: '. format (n)))
    if n % 2 == 0:
        soma += n
        cont += 1# = a cont = n + 1
print ('Você informou {} número(-s) PAR(-ES) e a soma deles é {}.'.format (cont, soma))     
          
         
#Desafio 51-PA de 10 números e soma
print ('=' * 25)
print ('     PA DE 10 TERMOS      ')
print ('=' * 25)
a1 = int (input ('Digite o primeiro termo da PA (a1): '))
r = int (input ('Digite a razão (r): '))
décimo = a1 + (10 - 1) * r # para descobrir o 10 termo 
soma = ((a1 + décimo) * 10) / 2
for c in range (a1, décimo + r, r):
    print ('{}'.format (c), end= ' > ') #primeiro termo a1 e pula a razão
print ('FIM')
print ('A soma dos 10 termos é igual a {}.'. format (soma)
       
       
#Desafio 52-número primo
num = int (input ('Digite um número: '))
tot = 0 #mostra o número de vezes qu eum número é divisivel e da resto 0

for c in range (1, num + 1):
    if num % c == 0:
        print ('\033[33m', end='')#se o número for divisível amarelo
        tot += 1 # é igual a tot = tot + 1 quantas vezes foi divisível
    else:
        print ('\033[31m', end='')#se não for divisível vermelho
    print ('{}'.format (c), end=' ')#pertece ao if e ao else, printa os divisiveis e não divisiveis
        
        
print ('\n\033[mO número {} foi divisível {} vezes.'.format (num, tot))#código para retirar a cor
if tot == 2:
    print ('E por isso ele É PRIMO!') 
else:
    print ('E por isso ele NÃO É PRIMO!')
       
       
#Desafio 53-palíndromo
'''frase = str (input ('Digite uma frase: ')).strip() .upper()
palavras = frase.split()#separa as palavras pelo espaço
junto = ''.join (palavras)#retira os espaços
inverso = ''#inverte as letras de junto

for letra in range (len (junto) - 1, -1, -1):#os -1 lê a string de trás para frente
    inverso += junto [letra]
print (" o inverso de {} é {}.".format (junto, inverso))
    
if inverso == junto:
    print ('A frase {} é um palíndromo.'.format (frase))
else:
    print ('A frase {} não é um palíndromo.'.format (frase))'''
              
#outra forma de fazer sem for        
frase = str (input ('Digite uma frase: ')).strip() .upper()
palavras = frase.split()#separa as palavras pelo espaço
junto = ''.join (palavras)#retira os espaços
inverso = junto [::-1] #inverte as letras do junto

print ('O inverso de {} é {}.'.format (junto, inverso))
    
if inverso == junto:
    print ('A frase {} é um palíndromo.'.format (frase))
else:
    print ('A frase {} não é um palíndromo.'.format (frase))
       
       
#Desafio 54-separar maiores e menores de idade
from datetime import date
atual = date.today().year
totmaior = 0#cpntadores
totmenor = 0

for dn in range (1,8):
    dn = int(input('Em que ano a {}ª pessoa nasceu? '.format (dn)))
    idade = atual - dn
    if idade >= 18:
        totmaior += 1
        print ()
    else:
        totmenor += 1
print ('Ao todo tivemos {} pessoas maiores e {} pessoas menores de idade.'.format (totmaior, totmenor))

#Desafio 55-menor e maior peso
maior = 0
menor = 0

for p in range (1, 6):
    peso = float (input('O peso da {}ª pessoa: '.format (p)))
    if p == 1:# se o maior e o menor peso estiver na primeira pessoa
        maior = peso
        menor = peso
    else:#verifica se não for a primeira pessoa
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
            
print ('O maior peso lido foi de {}Kg e o menor foi de {}Kg.'.format (maior, menor))
       
       
Desafio 56- analise detalhada
somaidade = 0 #inicialização das variáveis
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range (1,5):
    print ('----- {}ª PESSOA -----'.format (p))
    nome  = str (input ('Nome completo: ')) .strip() .upper()
    idade = int (input ('Idade? '))
    sexo  = str (input ('Sexo [M/F}: ')) .strip() .upper()
    somaidade += idade #somaidade = somaidade + idade
    
    if p == 1 and sexo == 'M':# se o homem mais velho é a primeira pessoa
        maioridadehomem = idade #considera a idade e não número de homens
        nomevelho = nome
        
    if sexo == 'M' and idade > maioridadehomem:# seu e não colocar upper no sexo tenho de fazer sexo in ('Mm')
        maioridadehomem = idade
        nomevelho = nome
        
    if sexo == 'F' and idade < 20:
        totmulher20 += 1 #qtde de mulher
        
médiaidade = somaidade / 4

print ('A média de idade do grupo é de {} anos.'.format (médiaidade))
print ('O homem mais velho tem {} e seu nome é {}.'.format (maioridadehomem, nomevelho))
print ('Ao todo são {} mulheres com menos de 20 anos.'.format (totmulher20))


#Aula 14- comando while
'''for c in range (1, 10):
    print (c)
print ('FIM')'''

#Usando while ( sei o limite: while ou for/ não sei o limite while)
'''c = 1
while c < 10:
    print (c)
    c += 1 # c = c + 1
print ('FIM')'''


'''n = 1
while n != 0: #enquanto n for diferente de 0
    n = int(input('Digite um valor: '))
    print (n)
print ('FIM')'''

''''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]: ')) .upper()
print ('FIM')'''

par = impar = 0
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:#para ele não contra o zero como par
        if n % 2 == 0 and n != 0:
            par += 1
        else:
            impar += 1
print ('Temos na sequência {} números pares e {} ímpares.'.format (par, impar))
print ('FIM')

       
#Desafio 57-digitar sexo corretamente
sexo = str(input('Informe seu sexo [M/F]:')) .upper() .strip()[0]#[0] só pego a primeira letra
while sexo not in 'MF':#faço assim porque é uma string
    sexo = str(input('Dados inválidos. Por favor informe seu sexo.'))
print ('Sexo {} registrado com sucesso.'.format (sexo))
       
#Desafio 58-jogo da adivinhação
print ('*' * 20)
print ('JOGO DA ADIVINHAÇÃO')
print ('*' * 20)

from random import randint
computador = randint (0, 10)#escolha do computador
print ('''Sou seu computador...
Acabei de pensar um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
acertou = False#enquanTO não acertou recebe false
palpites = 0 #contador de palpites

while not acertou:
    jogador = (int(input('Qual é o seu palpite? ')))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print ('Menos... Tente mais uma vez!')
        else:#poderia colocar elif jogador < computador
            print ('Mais... Tente mais uma vez!')
print ('Acertou com {} palpites. Parabéns!'.format (palpites))
       
       
#Desafio 59-menu de opções
from time import sleep#dá um intervalo entre os blocos
n1 = int (input ('Primeiro valor: '))
n2 = int (input ('Segundo valor:  '))
escolha = 0
while escolha != 6:#5 é para parar o programa
    print ('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa)''')

    escolha = (int (input ('>>>>> Qual é sua opção? ')))

    if escolha == 1:
        soma = n1 + n2
        print ('A soma entre {} e {} é {}.'.format (n1, n2, soma))
    
    elif escolha == 2:
        prod = n1 * n2 
        print ('O produto de {} por {} é {}'.format (n1, n2, prod))
    
    elif escolha == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print ('Entre {} e {} o maior número é {}.'.format (n1, n2, maior))
    
    elif escolha == 4:
        print ('Informe os números novamente: ')
        n1 = int (input ('Primeiro valor: '))
        n2 = int (input ('Segundo valor:  '))
    
    elif escolha == 5:
        print ('Finalizando...')
        
    else:
        print ('Opção inválida! Tente novamente.')
    print ('=-=' * 10)
    sleep (2)
        
print ('Fim do programa. Volte sempre!')

       
#Desafio 60-
'''from math import factorial
num = int (input ('Digite um número para saber o fatorial: '))
f = factorial (num)
print (' O fatorial de {} é {].'.format (num, f))'''

#outra forma
n = int (input ('Digite um número para saber o fatorial: '))
c = n # o fatorial de 5! é 1x2x3x4x5
f = 1 #fator nulo de multiplicação
print ('Calculando {}! = '.format (n), end ='')
while c > 0:
    print ('{}'.format (c), end ='')
    print (' x ' if c > 1 else ' = ', end ='') #imprime o sinal de x e imprimi = quando acaba
    f = f * c # f *= c 3! = 1 (c-2) . 2 (c-1). 3 (c)
    c = c - 1 # c -= 1
print ('{}'.format (f))

#Desafio 61-PA com estrutura while
print ('=-=' * 8)
print ('Programa gerador de PA')
print ('=-=' * 8)
primeiro = int (input('Primeiro termo: '))
razão  = int (input ('Razão da PA: '))
termo = primeiro #começa com o primeiro
último = int (input('Último termo: '))
cont = 1#conta os termos
while cont <= último:
    print ('{} > '.format (termo),end ='')# retiro o final da linha com end = ''
    termo = termo + razão
    cont += 1 # cont = cont + 1
print ('FIM')

#Desafio 62-Super PA
print ('=-=' * 8)
print ('Programa gerador de PA')
print ('=-=' * 8)
primeiro = int(input('Primeiro termo: '))
razão  = int(input ('Razão da PA: '))
termo = primeiro #começa com o primeiro
cont = 1#conta os termos
total = 0#super PA
mais = 10#super PA quantos termos a mais vc quer, além dos 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print ('{} > '.format (termo),end ='')# retiro o final da linha com end = ''
        termo = termo + razão
        cont += 1 # cont = cont + 1
    print ('PAUSA')#esse bloco faz com 10

    mais = int(input('Quantos termos você quer mostrar a mais? '))#a partir daqui acrescenta números
    print ('Progressão finalizada com {} termos mostrados'.format (total))
print ('FIM')

       
#Desafio 63-sequencia de Fibonacci
print ('#' * 22)
print ('Sequência de Fibonacci')
print ('#' * 22)

n = int(input('Quantos termos você quer mostrar: '))
t1 = 0
t2 = 1
print ('{} > {}'.format (t1, t2), end='')
cont = 3
while cont <= n:# repete o núemro de vezes n
    t3 = t1 + t2
    print (' > {}'.format (t3), end='')
    t1 = t2 # t1 passa ser o t2 
    t2 = t3 # t2 passa ser t3
    cont  += 1
print (' > FIM')
print ('#' * 22)


 #Desafio 64 tratando varios valores
#pode se fazer cont = soma = n = 0
cont = 0
soma = 0
n = 0
while n!= 999:
    n = int(input('Digite um número [999 para parar]: '))
    soma += n
    cont += 1
    if n == 999:
        print ('FIM')
print ('#' * 45)
print ('Você digitou {} números e soma entre eles é {}.'.format (cont - 1, soma - 999))
print ('#' * 45)

'''#solução Guanabara para evitar problemas para não considerar 0 999
cont = soma = n = 0
n = int(input('Digite um número [999 para parar]: '))
while n!= 999:
    soma += n
    cont += 1
    n = int(input('Digite um número [999 para parar]: '))
print ('#' * 45)
print ('Você digitou {} números e soma entre eles é {}.'.format (cont, soma))
print ('#' * 45)'''

#Desafio 65
resp = 'S'
média = qtde = soma = maior = menor = 0#pode escrever separado

while resp in 'Ss':  # pode usar s maiúsculo ou minúsculo
    num = int(input('Digite um número: '))
    soma += num
    qtde += 1
    if qtde == 1:# no primero numero que vc digitou
        maior = menor = num
    else:
        if num > maior: # se o numero recém digitado for maior que o maior que já tinha sido digitado
            maior = num
        if num < menor: # o contrário
            menor = num
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]# [0] considera só a primeira letra

média = soma / qtde
print('Você digitou {} números e a média foi {:.2f}.'. format (qtde, média))
print ('O maior valor foi {} e o menor foi {}.'.format (maior, menor))
print('Acabou')

       
# aula 15-interrompendo repetições

'''cont = 1
while True:
    print (cont, '->', end='')
    cont += 1
print ('acabou')'''  # looping infinito

'''n = soma = 0
while n != 999:#999 é um flag ponto de parada
    n = int(input('Digite um número: '))
    soma += n
print ('A soma vale {}.'.format (soma))'''

# fazer o de cima sem gambiarra
'''n = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:  # o 999 não será somado
        break
    soma += n
# print ('A soma vale {}.'.format (soma))
print(f'A soma vale {soma}')  # f strings'''

nome = 'André'
idade = 45
salário = 965.6
print(f'Meu nome é {nome}, tenho {idade} e ganho R${salário:.2f}.')

       
 #Desafio 66
cont = soma = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    cont += 1
    soma += n
#print (f' A soma dos {cont} digitados é {soma}.)
print ('A soma dos {} números digitados é {}.'.format (cont, soma))

#Desafio 67-tabuada de va´rios números       
n = 0
while True:
    print('*' * 72)
    n = int(input('Quer ver a tabuada de qual valor (qualquer nº negativo para parar)?  '))
    print('*' * 72)
    if n < 0:
        break
    for c in range(1, 11):
        prod = c * n
        #print('{} x  {} = {} '.format(c, n, prod))
        print(f'{c} * {n} = {prod}')
       
# Desafio 68-par ou ímpar
from random import randint
contvitoria = 0

while True:
    n = int(input('Digite um número de 1 a 10:  '))
    comput = randint(0, 10)
    res = n + comput
    tipo = ' '  # par ou impar
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar: [P/I]: ')).strip().upper()[0]
    print('Você jogou {} e o computador {}. O total é {}.'.format(n, comput, res))

    if tipo == 'P':
        if res % 2 == 0:
            print('Você VENCEU!')
            contvitoria += 1
        else:
            print('Você PERDEU')
            break #parada derrota

    elif tipo == 'I':
        if res % 2 == 1:
            print('Você VENCEU!')
            contvitoria += 1
        else:
            print('Você PERDEU!')
            break

    print('Vamos jogar novamente...')

print('GAME OVER! Você venceu {} vezes.'.format(contvitoria))
       
#Desafio 70
       
tot18 = tothomem = totmulher20 = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        tothomem += 1
    if sexo == 'F' and idade < 20:
        totmulher20 += 1
    print('-' * 20)
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break
    print('-' * 20)
print('Total de pessoas com mais de 18 anos: {}'.format(tot18))
print('Total de homens: {}'.format(tothomem))
print('E temos {} mulher(-es) com menos de 20 anos'.format(totmulher20))

       
Desafio 70-estatística de produto
print('=-=' * 6)
print('LOJA SUPER BARATÃO')
print('=-=' * 6)
total = tot1000 = menor = cont = 0
barato = ' ' #nome do poduto mais barato
while True:
    prod = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço < 1000:
        tot1000 += 1
    if cont == 1 or preço < menor: #menor preço for primeiro prod cont == 1
        menor = preço
        barato = prod
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

print('{:-^40}'.format('FIM DO PROGRAMA'))  # centraliza com 40 espaços
print(f'O total da compra foi de R$ {total:.2f}.')
print(f'{tot1000} itens custaram mais de R$ 1000.00.')
print(f'O produto mais barato foi {barato} e custa R$ {menor:.2f}.')
       
       
#Desafio 45-Game pedra papel e tesoura
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
print ('''Sua opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

computador = randint (0,2)
jogador = int(input('Qual sua jogada?' ))

print('JO')
sleep(1)
print ('KEN')
sleep(1)
print ('PO!!!')
sleep(1)

print ('=-=' *11)
print ('Computador jogou {}.'.format(itens[computador]))#faz para converter o número nno item
print ('Jogador jogou {}.'.format (itens[jogador]))
print ('=-=' *11)

if computador == 0:
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('O jogador vence!')
    elif jogador == 2:
        print('O computador vence!')
    else:
        print ('Jogada inválida!')
        
elif computador == 1:
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('O jogador vence!')
    elif jogador == 2:
        print('O computador vence!')
    else:
        print ('Jogada inválida!')
    
elif computador == 2:
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('O jogador vence!')
    elif jogador == 2:
        print('O computador vence!')
    else:
        print ('Jogada inválida!')
       

#Desafio 71-caixa eletrônico
print('=' * 30)
print('{:^30}'.format('BANCO CEV'))  # comando para centralizar
print('=' * 30)
valor = int(input('Quanto você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédula(-s) de R${céd}.')
        elif céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
