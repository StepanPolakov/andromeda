import random
cars_counter=0
summa=0
number_counter=0
iterations=0
for i in range(10**6):
    car_number=random.randint(0,999)
    cars_counter+=1
    number_counter+=car_number
    if number_counter>=1000:
        summa+=cars_counter
        cars_counter=0 
        number_counter=0
        iterations+=1
print(summa/iterations )