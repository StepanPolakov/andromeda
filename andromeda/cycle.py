
##counter=1
##while True:
##     while counter<=100:
##        print (counter)
##        counter+=1
##     while counter >=0:
##        print(counter)
####        counter-=1
##rain=True
##while rain==True:
##    print ('я сижу дома')
##    stop= input('дождь закончился?')
##    if stop=='да':
##         print('ура')
##         break
##number=1
##while 20>number:
##    print(number)
##    number+=1
##for number in range(20):#диапазон до 20
##    print(number)
##print(list(range(1,15)))
##for i  in range(5):
##    start=input('с какого числа вывести диапазон?')
##    n=input('до какого числа вывести диапазон?')
##    n=int(n)
##    start=int(start)
##    print(list(range(start,n+1)))
##group=[]
##for i  in range(5):
##    name=input('как тебя зовут?')
##    print(f'привет,{name}')
##    group.append(name)
##    print(group)
def Steam():
    print('магазин игр Steam')
    flag=True
    wish_list=[]
    while flag:
        print('Добро пожаловать!')
        print('Выбери действие:\n1-добавить игру\n2-удалить игру\n3-вывести все игры\n4-выйти из программы')
        action=input('->')
        if action=='1':
            game=input('какую игру ты бы хотел?')
            if game not in wish_list:
                wish_list.append(game)
                print(f'{game} добавлена')
            else:
                print('эта игра уже есть')
        
        elif action=='2':
            game=input('какую игру ты удаляешь из желаемого?')
            if game  in wish_list:
                wish_list.remove(game)
                print(f'{game} удалена')
            else:
                print('этой игры нет')
        elif action=='3':
            if len(wish_list)==0:
                print('здесь пока ничего нет')
            else:
                print(f'список желаний:{wish_list}')
        elif action=='4':     
            flag=False
            print('спасибо за использование программы')
            break
        input('нажмите Enter,тобы продолжить')
    
        
