import random
def game():
   name =input ('Ваше имя:')
   print(f'{name}, компьютер загадал число от 1 до 100.Отгадай за 10 попыток.')
   secret_number=random.randint(1,100)
   tries=10
   while tries>0:
      print(f'попыток осталось:{tries}')
      tries-=1
      user_number=input('Введите число:')
      user_number=int(user_number)
      if secret_number==user_number:
         print(' Ты победил!')
         break
      elif secret_number<user_number:
         print('ваше число больше компьютера')
      elif secret_number>user_number:
         print('ваше число меньше компьютера')        
      if tries==0:
         print(' Ты проиграл!')
         break
