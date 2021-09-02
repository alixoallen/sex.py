cont=0
cont1 = 1000
for c in range (1,6):
    n = float(input('peso da {} pessoa: '.format(c)))
    if n>cont:
        cont=n
    if n<cont1:
        cont1=n
print('O menor peso é {}Kg e o maior peso é {}Kg'.format(cont1,cont))