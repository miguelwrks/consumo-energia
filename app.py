print('--> Programa Consumo de energia! <--\n')

aparelho = str(input("Digite o nome do aparelho: "))

potencia = float(input('\nDigite a potência do aparelho em Watts (W): ')) #float pra n dar nenhumm problema

usoHoras = float(input("\nDigite o tempo médio de uso diário do aparelho em horas: "))

#calcular consumo mensal em kWh
# consumo sendo: potencia multiplicado por horas ao dia vezes 30 (um mes) e dps tudo isso dividido por mil (para dar o k do kWh [quilo watt])
#add custo estimado por valor fixo (0,75 por kwh), ai nisso eh so multiplicar esse 0,75 pelo consumo mensal e ai sai o valor
