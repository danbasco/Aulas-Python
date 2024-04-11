'''
Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. 
A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

Entrada
O arquivo de entrada contém 2 números inteiros e 1 número com duas casas decimais, representando o número, 
quantidade de horas trabalhadas e o valor que o funcionário recebe por hora trabalhada, respectivamente.

Saída
Imprima o número e o salário do funcionário, conforme exemplo fornecido, com um espaço em branco antes e depois da igualdade. 
No caso do salário, também deve haver um espaço em branco após o $.

'''

numero = int(input())
horas = int(input())
valor = float(input())


print("NUMBER =", numero)
print(f"SALARY = U$ {(horas*valor):.2f}") # Note que é preciso utilizar o :.2f para determinar a quantidade de casas decimais que o valor vai printar



'''
Para substituir uma variável dentro do print sem usar a virgula, é necessário incluir o f antes das "", para aceitar variáveis, funções e códigos
dentro do print.

Exemplo:

nome = "João"
print(f"Seu nome é {nome}.")

'''
