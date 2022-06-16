####summa=0
####for i in range(1,101):
####    summa+=i
####print (summa)
####fact=1
####for i in range(1,21):
####    fact*=i
####print(fact)
##books=['Ночной дозор','Властелин колец','Звездные войны']
##print(books[1])
##length=len(books)
##for i in range(length):
####    print(i+1)
####    print(books[i])
##    print(f'{i+1}.{books[i]}')
##def write():
##    print('Степан')
##write()   
##write()    
##write()
def robot_forvard():
    print('Poбот идёт вперёд')
def robot_backward():
    print('Poбот идёт назад')
def robot_left():
    print('Poбот идёт влево')
def robot_right():
    print('Poбот идёт вправо')
def robot_jump():
    print('Poбот прыгает')
backpack=[]  
def robot_take(item):
    return item
    print(f'Poбот берёт {item}')
def robot_put(item,backpack):
    if item in backpack:
        print(f'Poбот кладёт {item}')
        backpack.remove(item)
    else:
        print('Класть нечего')
while True:
    key=input('Нажмите на клавишу')
    if key=='a':
        robot_left()
    if key=='d':
        robot_right()
    if key=='w':
        robot_forvard()
    if key=='s':
        robot_backward() 
    if key==' ':
        robot_jump()
    key=input('Какая команда:')    
    if key=='f':
         thing=input('Что брать?')
         robot_take(thing)
    elif key.startswith('возьми'):
        words=key.split()
        thing = robot_take(words[1])#то,что робот берет, сохраняем
        backpack.append(thing)
        print (backpack)
    if key=='q':
        thing=input('Что положить?')
        robot_put(thing, backpack)
    elif key.startswith('положи'):
        words=key.split()#список ["положи", "что именно"]
        robot_put(words[1],backpack)
