def print_hi(name):

    print(f'Hi, {name}')

a = input()
i = 0
j = len(a) - 1
while i<j:
    if a[i] != a[j]:
        break
    else:
        i+=1
        j-=1
        print('YES')

r = a[::-1]
if a == r:
    print('YES')
else:
    print('NO')


if __name__ == '__main__':
    print_hi('PyCharm')