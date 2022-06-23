#XOR=исключающий или
#1^1=0
#0^0=0
#1^0=1
#0^1=1
# a=10
# b=5
# a=a^b#1010^0101=1111
# print(a)
# b=a^b#1111^0101=1010
# print(b)
# a=a^b
# print(a,b)


import re


def crypt_password(password,key):
    '''
    Шифрование пароля
    '''
    crypt=''#зашифрованный пароль
    for bukva in password:
        print(ord(bukva))
        crypt+=chr(ord (bukva)^key)
    return (crypt)
crypt_password('Фчакеи', 5)

