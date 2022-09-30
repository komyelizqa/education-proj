def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')
a = int(input())
while a <= 100:
    if a >= 10:
        print(a)
        a = int(input())
    else:
        a = int(input())
        continue

    if __name__ == '__main__':
            print_hi('PyCharm')