from itertools import cycle
import random
import number_game
import mortal_kombat
import cycle
import cows_and_bulls
KEY=3
def crypt_password(password,key):

    crypt=''#зашифрованный пароль
    for bukva in password:
        #print(ord(bukva))
        crypt+=chr(ord (bukva)^key)
    return (crypt)

def registration():

    '''
    Реггистрация нового пользователя
    '''
    print('Давайте я вас запишу в список пользователей')
    login= input('введите ваш логин: ')
    password=input('введите ваш пароль:')
    
    file = open('logins.txt', mode='a',encoding='utf-8')
    file.write(f'{login}'+' ')
    file.close()

    file = open('passwords.txt', mode='a',encoding='utf-8')
    file.write(f'{crypt_password(password,key=3)}'+ ' ')
    file.close()

def read_users(filename):
    file = open(filename, mode='r',encoding='utf-8')  
    data=file.read()  
    file.close()
    return data.split()

def sign_in(flag): 
    login_list=read_users('logins.txt')
    password_list=read_users('passwords.txt')

    login= input('введите ваш логин: ')
    print(f'вы ввели {login}')
    password=input('введите ваш пароль:')
    print(f'Логин: {login}, пароль: {password}')
    
    if login in login_list and crypt_password(password,key=KEY) in password_list:
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
    return flag,login

def chat(login):
    file = open('chat.txt', mode='r',encoding='utf-8')
    data=file.read()
    print(data)
    file.close()
    file = open('chat.txt', mode='a',encoding='utf-8')#append
    while True:
        your_message=input('Сообщение:')
        if your_message=='exit':
            break
        file.write(f'\n{login}:{your_message} ')
    file.close()

login_list=read_users('logins.txt')#список логинов
password_list=read_users('passwords.txt')#список паролей

    
flag=False
while True:#до тех пор пока заблокировано
    if flag==False:#если мы не вошли
        way=input('Что вы хотите сделать? 1-зарегистрироваться ,2-войти ')
        if way=='1':
            registration()
        if way=='2': 
            flag, login = sign_in(flag) 
    else:#если уже вошли
        print()  
        way=input('Что вы хотите сделать? 1-выйти из аккаунта 2-выйти из программы,3 - открыть чат,4-поиграть в игру угадай число,5-посмотреть мортал комбат,6-зайти в магазин игр Steam,7- поиграть в быки и короровы>>>''')
        if way=='1':
            flag= False
        elif way=='2':
            print('Всего доброго!')
            break
        elif way=='3': 
            chat(login)
        elif way=='4':
            number_game.game()
        elif way=='5':
            mortal_kombat.figting()
        elif way=='6':
            cycle.Steam() 
        elif way=='7':
            cows_and_bulls.cows_bulls()
# if flag==True:  
#     vegetables=116
#     children=23
#     print (vegetables//children)
#     money=38564
#     bublegum=17
#     print(money//bublegum)
#     print(f'Саша купит {money//bublegum} жевачек')
#     print(f'останется {money%bublegum} рублей')
#     money=5000
#     fruits=60/2+20*3
#     fruits_with_sale=0.8*fruits
#     sweets=500
#     print(money-fruits_with_sale-sweets)
#     money=700
#     note=35+0.1*35
#     print(money//note)
#     print(f'масимум {money//note} блокнотов')
#     bread='батон'
#     eggs=True
#     if eggs==True:    
#         print(10*bread)