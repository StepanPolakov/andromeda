class Phone:
    # model='Nokia'#характеристика(атрибут)
    # oper_system='Android'
    # battery=5000
    def __init__(self,model,oper_system):
        self.model=model
    def take_photo(self):
        print(f'{self.model} делает фотку')

phone1=Phone(model='Nokia',oper_system='Android')
print(phone1.model)
phone2=Phone(model= 'Motorola',oper_system ='Android')
print(phone2.model)

phone1.take_photo()
phone2.take_photo()







class monster:
    def __init__(self,name,look,weapon,weakness):
        self.name=name
        self.look=look
        self.weapon=weapon
        self.weakness=weakness
    def search(self):
        print(f'{self.look}{self. name} ищет тебя...')

class Student:
    def __init__(self,):