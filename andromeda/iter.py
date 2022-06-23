# fruits=['яблоко','груша','апельсин','банан']
# for item in fruits:
#     print (item)
# fruits=iter(fruits)
# print (fruits)
# print(next(fruits))
# apple=(next(fruits))
# orange=(next(fruits))
# banana=(next(fruits))
# name='итерация'
# name=iter(name)
# print(next(name))
# print(next(name))
# print(next(name))
# # print(next(name))
# import numbers
# import time
# duz=['дуц']*5
# daz=['дац']*5
# duz=iter(duz)
# daz=iter(daz) 
# def party():
#     print(next(duz)) 
#     print(next(daz)) 
#     time.sleep(1)
# for i in range(5):
#     party()
import time
class Number:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        b=self.a 
        self.a +=1
        return b
number=Number()
number=iter(number)
for i in range(5):
    time.sleep(2)
    print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))