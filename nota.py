n1=float(input('digite sua primeira nota:'))
n2=float(input('digite sua segunda nota:'))
a=(n1+n2)/2
if (a>=7):
    print('com a nota de {}, e {}, sua media foi de {}, assim voce esta aprovado'.format(n1,n2,a))
elif (a>=5.0 and a<= 7):
    print('com a nota {}, e de {}, sua media foi de {}, logo voce ficou de recuperação'.format(n1,n2,a))
else:
    print('com as notas de {}, e {}, sua media foi de {}, logo voce foi reprovado'.format(n1,n2,a))