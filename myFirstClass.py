def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    figure = input()
    if figure =='круг':
        r=int(input())
        print(r**2*3.14)
    elif figure=='прямоугольник':
        a=int(input())
        b=int(input())
        print(a*b)
    elif figure =="треугольник":
        a = int(input())
        b = int(input())
        c = int(input())
        P=(a+b+c)
        p=P/2
        print((p*(p-a)*(p-b)*(p-c))**0.5)





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
