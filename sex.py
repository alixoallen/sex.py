
sex=str(input('digite seu sexo : [M/F]')).upper().strip()[0]
while sex not in 'MmFf':
   sex=str(input('dados invalidos, tente novamente :')).strip().upper()[0]
print('sexo {} registrado com sucesso'.format(sex))
