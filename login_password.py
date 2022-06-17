import random
coin=random.randint(1,2)
if coin==1:
    print ('решка')
else:
    print ('орёл')
flag=False
while flag==False: 
    login= input('введите ваш логин: ')
    print(f'вы ввели {login}')
    password=input('введите ваш пароль:')
    print(f'вы ввели {login} и {password}')

    if login=='stepan' and password=='c' :
        print('вы вошли в свой гитхаб')
        flag=True
    elif login=='vanya' and password=='69420' :
        print('вы вошли в свой гитхаб')
        flag=True
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

