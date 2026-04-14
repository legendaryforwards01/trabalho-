
dia = int(input('Entre com o dia'))
mes = int(input('Entre com o mês'))
ano = int(input('Entre com o ano'))
pd = 0
pm = 0
pa = 0

if (ano % 4 == 0 and ano%100 != 0) or (ano%400==0):
    bissexto = True
else:
    bissexto = False
if (mes==1 or mes==3 or mes==5 or mes==7 or mes == 8 or mes == 10):
    mes31 = True
else:
    mes31 = False
if (mes==4 or mes==6 or mes==9 or mes==11):
    mes30 = True
else:
    mes30 = False
    
    
while (dia>31 or mes>12 or dia<=0 or mes<=0 or ano<=0) or (dia>30 and (mes30)) or (mes==2 and dia>29 and (bissexto) or (mes==2 and dia>28 and not(bissexto))):
    print ('Erro! Essa data não existe.')
    dia = int(input('Entre com o dia'))
    mes = int(input('Entre com o mês'))
    ano = int(input('Entre com o ano'))
    
if (dia==31) and (mes == 12):
    pd= 1
    pm = 1
    pa = ano+1
    print(f'{pd}/{pm}/{pa}')
elif(dia==31 and (mes31)):
    pd= 1
    pm = mes+1
    pa= ano
    print(f'{pd}/{pm}/{pa}')
elif(dia==30 and (mes30)):
    pd= 1
    pm = mes+1
    pa= ano
    print(f'{pd}/{pm}/{pa}')
elif(dia==28 and mes ==2):
     if (bissexto):
         pd=dia+1
         pm=mes
         pa=ano
         print(f'{pd}/{pm}/{pa}')
     else: 
         pd=1
         pm=mes+1
         pa=ano
         print(f'{pd}/{pm}/{pa}')
elif(dia==29 and mes==2):
    if (bissexto):
        pd=1
        pm=mes+1
        pa=ano
        print(f'{pd}/{pm}/{pa}')
    else: 
        print ('Erro! Essa data não existe.')
else:
    pd= dia +1
    pm = mes
    pa = ano
    print(f'{pd}/{pm}/{pa}')
    
