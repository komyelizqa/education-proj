# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    a=float(input())
    b=float(input())
    c=input()
    if c == '+':
        print(a+b)
    elif c == '-':
        print(a-b)
    elif c=='/' and b==0:
        print('Деление на 0!')
    elif c == '/':
        print(a / b)
    elif c=='*':
        print(a*b)
    elif c == 'mod'and b==0:
        print('Деление на 0!')
    elif c=='mod':
        print(a%b)
    elif c=='pow':
        print(a**b)
    elif c=='div' and b==0:
        print('Деление на 0!')
    elif c=='div':
        print(a//b)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
