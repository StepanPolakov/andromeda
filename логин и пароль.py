import random
coin=random.randint(1,2)
if coin==1:
    print ('решка')
else:
    print ('орёл')
flag=False
while flag==False:#о тех пор пока заблокировано 
    login= input('введите ваш логин: ')
    print(f'вы ввели {login}')
    password=input('введите ваш пароль:')
    print(f'вы ввели {login} и {password}')

    if login=='stepan' and password=='stepler0004' :
        print('вы вошли в свой гитхаб')
        flag=True#система разблокированна
    elif login=='vanya' and password=='69420' :
        print('вы вошли в свой гитхаб')
    elif password==''and password =='':
        print('вы не ввели и логин,и пароль')
    elif password=='':       
        print('вы не ввели пароль')
    elif login=='':
       
        print('вы не ввели логин')   
    else:
        chanse=random.randint(1,2)
        if chanse==1:
            print('ха ха, не верно')
        elif chanse==2:
            print('Ты не пройдёшь!')

if flag==True:  
    vegetables=116
    children=23
    print (vegetables//children)
    money=38564
    bublegum=17
    print(money//bublegum)
    rint(f'Саша купит {money//bublegum} жевачек')
    print(f'останется {money%bublegum} рублей')
    money=5000
    fruits=60/2+20*3
    fruits_with_sale=0.8*fruits
    sweets=500
    print(money-fruits_with_sale-sweets)
    money=700
    note=35+0.1*35
    print(money//note)
    print(f'масимум {money//note} блокнотов')
    bread='батон'
    eggs=True
    if eggs==True:    
        print(10*bread)
 
