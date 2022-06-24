color='blue'
def func():
    global color
    color='red'
    print (f'Внутри {color}')
    return color
if __name__=='__main__':
    print (f'Снаружи {color}')    
    func()
    print (f'Снаружи {color}')
