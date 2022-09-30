def print_hi(name):
    print(f'Hi, {name}')
# система уравнений
def f(x):
    if x<=-2:
        f=1-(x+2)**2
    elif x > -2 and x<= 2:
        f = x/2 * (-1)
    elif x > 2:
        f = (x-2)**2 + 1
    return f

if __name__ == '__main__':
    print_hi('PyCharm')