
import random
import cowsay



def cows_bulls():
    import random
    cowsay.turtle('''Компьютер загадал четырёхзначное число.Твоя задача- отгадать.
    Если угадал число-это корова,
    если угадал место-бык''')
    number=random.randint(1000,9999)
    number=str(number)
    while True:
        user_number=input('Введите своё число:')
        list =[]
        cows=0 
        bulls=0
        for letter in number:
            list.append(letter)
        for letter in user_number:
            if letter in list:
                cows+=1
                #print(number,user_number,cows)
        for i in range(4):
            if user_number[i] ==list[i]:
                bulls+=1
                cows-=1
        cowsay.turtle(f'У вас {cows} коров и {bulls} быков')
        if  bulls == 4:
            cowsay.turtle('Вы победили!') 
            break
if __name__=='__main__':
    cows_bulls()