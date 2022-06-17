file = open('text.txt', mode='w',encoding='utf-8')
for i in range(3):

    file.write('Привет,мир!\n')
    file.write('Привет,Ваня!\n')
file.close()
import os
if'файлики'not in os.listdir():
    os.mkdir('файлики')

# for i in range(3):
#     file = open(f'файлики/ text_{i}.txt', mode='w',encoding='utf-8')
#     file.write('Привет,мир!\n')
#     file.write('Привет,Ваня!\n')
#     file.close()
file = open(f'файлики/ text_0.txt', mode='r',encoding='utf-8')  
data=file.read().split(' ')
file.close()
print(data)

for i in range(len(data)):
    if i==0:
       data[i]=1
    data[i]=int(data[i])
print (data)