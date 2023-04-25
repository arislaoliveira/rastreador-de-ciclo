import datetime

print('Olá! Vou te auxiliar a rastrear seu ciclo menstrual! 🩸')
ultima = datetime.datetime.strptime(input('Informe a data da sua última menstruação: '), '%d/%m/%Y').date()
hoje = datetime.date.today()
ciclo = (hoje - ultima).days

if ciclo > 28:
    print('Seu período parece estar {} dias atrasado.'.format(ciclo - 28))
elif 14 >= ciclo <= 20 != 19:
    print('Parece que você está no período fértil!')
elif ciclo == 19:
    print('Parece que você está ovulando!')
elif 20 < ciclo < 28:
    print('Parece que você está no período pré-menstrual!')
else:
    print('Seu período está dentro das conformidades!')

print('\nOs valores são estimados com base na convenção de que o ciclo menstrual dura 28 dias, no entanto é sempre importante consultar um especialista!')