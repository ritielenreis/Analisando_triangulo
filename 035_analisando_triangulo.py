print('=' * 40)
print('Analisando triângulos')
print('=' * 40)
reta1 = float(input('Qual a medida da primeira reta? '))
reta2 = float(input('Qual a medida da segunda reta? '))
reta3 = float(input('Qual a medida da terceira reta? '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os segmentos informados PODEM formar um triângulo')
else:
    print('Os segmentos informados NÃO PODEM formar um triângulo')