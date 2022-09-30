

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

x=int(input())
y=x//100000+x%10000//1000+x%100000//10000
z=x%10+x%100//10+x%1000//100
if y==z:
    print('Счастливый')
else:
    print('Обычный')

    if __name__ == '__main__':
        print_hi('PyCharm')