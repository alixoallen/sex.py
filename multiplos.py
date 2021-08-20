soma=0
for x in range (1,501,2):
    if  (x%3==0) :
        soma+=x
        print(x)
print('a soma de tudo é {} '.format(soma))