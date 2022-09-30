def print_hi(name):
    print(f'Hi, {name}')

lst = [int(i) for i in input().split()]
count = 0
symbol_repeat = int(input())

for i in range(len(lst)):
    if symbol_repeat == lst[i]:
        print(i, end=' ')

    if symbol_repeat not in lst:
        print('Отсутствует')



if __name__ == '__main__':
    print_hi('PyCharm')