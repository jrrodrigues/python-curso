## Execício 011
## ------------
## Pintando Parede
#####
print('Calcular a quantidade de tinta por metro quadrado de parede que será pintada.')
print('')
ltParede = float(input('Digite a largura da parede: '))
alParede = float(input('Digite a altura  da parede: '))

dmParede = ltParede * alParede

qtTinta  = dmParede / 2

print('A dimensão da parede tem {} m2.'.format(dmParede))
print('Gastará {} litros de tinta para pinta-la.'.format(qtTinta))

