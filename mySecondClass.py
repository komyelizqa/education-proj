def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    a = int(input())
    if a >=11 and a<=14 or a % 100 == 11 or a % 100 == 12 or a % 100 == 13 or a % 100 == 14 and a<=1000 and a >=0:
        print(a, 'программистов')
    elif a % 10 == 1 and a<=1000 and a >=0:
        print(a, 'программист')
    elif a % 10 == 2 or a % 10 == 3 or a % 10 == 4 and a<=1000 and a >=0:
        print(a, 'программиста')
    elif a<=1000 and a >=0:
        print(a, 'программистов')




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')