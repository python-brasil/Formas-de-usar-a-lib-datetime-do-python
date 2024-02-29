import datetime

'''
Python Brasil
A MELHOR COMUNIDADE DE PYTHON DO BRASIL🐍

Abaixo poderá encontrar algus comandos da biblioteca datetime na qual é de grande utilidade caso
necessite trabalhar com calendário em seu código.

Abordagem com exemplos de uso da lib datetime
'''


# Momento exato
agora = datetime.datetime.now()
print(f'Momento exato: {agora}')

# Forma específica
data_hora = datetime.datetime(2024, 2, 25, 14, 15, 0)
print(f'Data e hora específica: {data_hora}')

# Data atual
hoje = datetime.date.today()
print(f'Apenas a data atual: {hoje}')


# Dia da semana
data = datetime.date(2024, 7, 1)
dia_semana = data.weekday()
# Domingo é 0, sabádo é 6
print(f'Dia da semana: {dia_semana}')

# Intervalo entre datas
data = datetime.date(2023, 12, 25)
intervalo = datetime.timedelta(days=7)
data_nova = data + intervalo
print(f'Adicionando um intervalo a data: {data_nova}')

# Diferença entre duas datas
data1 = datetime.date(2023, 1, 1)
data2 = datetime.date(2024, 1, 1)
diferenca = data2 - data1
print(f'Diferença entre duas datas: {diferenca.days}')