while True:
    num1=input('Введите первое число:')
    num1=int(num1)
    opperator=input('Введите знак:')
    num2=input('Введите второе число:')
    num2=int(num2)
    def plus(a,b):
        return a+b
    def minus(a,b):
        return a-b
    def multipl(a,b):
        return a*b
    def divide(a,b):
        return a/b
    if opperator =='+':
        answer=plus(num1,num2)
        print(f'Ответ:{answer}')
    if opperator =='-':
        answer=minus(num1,num2)
        print(f'Ответ:{answer}')
    if opperator =='*':
        answer=multipl(num1,num2)
        print(f'Ответ:{answer}')
    if opperator =='/':
        answer=divide(num1,num2)
        print(f'Ответ:{answer}')
    stop=input('Закончить?')
    if stop=='да':
        break












##def func2(a):
##    return a*2
##print(func2(5))
