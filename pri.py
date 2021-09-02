a=int(input('digite um valor: '))
x=0
for w in range(1, a+1):
    if a % w ==0:
        x += + 1
if x==2:
    print('é primo')
else:
    print('nao é primo')