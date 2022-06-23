


class Dog:
    def __init__(self,name,gender,breed):
        self.name=name
        self.gender=gender
        self.breed=breed
    def hobby(self):
        if self.name=='Шарик':
            print('Любит играть с мячом')
        elif self.name=='Бобик':
            print('Любит есть') 
    def work(self):
        for i in range(5):
            print(f'{self.name} спит')
        print(f'{self.name} проснулся')

 sharik=Dog(name='Шарик',gender='м',breed='Овчарка')
# print(sharik.name)
# print(sharik.breed)
 bobik=Dog(name='Бобик',gender='м',breed='Такса') 
# print(bobik.name)
# print(bobik.breed)
# sharik.hobby()
# bobik.hobby()
# sharik.work()


class Poppy(Dog):
    def __init__(self,name,gender,breed,host):
      super().__init__(self,name,gender,breed)
      self.host=host
def hobby(self):
    Dog.hobby(self)
    print('Любит пить воду')
    
sharik=Poppy('Шарик','Овчарка','м')
sharik.hobby()