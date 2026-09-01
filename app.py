import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()
print('--> Programa Consumo de energia! <--\n')

aparelho = str(input("Digite o nome do aparelho: "))

potencia = float(input('\nDigite a potência do aparelho em Watts (W): ')) #float pra n dar nenhumm problema

usoHoras = float(input("\nDigite o tempo médio de uso diário do aparelho em horas: "))


consumo = (usoHoras*30*(potencia))/1000

#preço a pagar medio
custo_estimado = (consumo)*0.75


clear()
print ('Aparelho --> ',aparelho)
print('O consumo foi de -->',consumo, 'kWh/mes')
print('O custo estimado e de --->', custo_estimado,'R$')
print('Programa desenvolvido por ---> Miguel Silva Gonçalves')
