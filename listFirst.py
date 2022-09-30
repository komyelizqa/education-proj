def print_hi(name):

    print(f'Hi, {name}')

a = [int(i) for i in input().split()]
b =  [1]*len(a)
if len(a)==1:
    print(a[0])
elif len(a)==2:
    print(a[1]*2, a[0]*2)
else:
    for i in range(0, len(a) - 1):
        b[i] = a[i - 1] + a[i + 1]
    b[len(a) - 1] = a[len(a) - 2] + a[0]

    for j in b:
        print(j, end=' ')


numbers = [int(i) for i in input().split()]
if len(numbers) == 1:
    print(numbers[0])
else:
    for i in range(len(numbers)):
        print(numbers[i - 1] + numbers[(i + 1) % len(numbers)], end=" ")

if __name__ == '__main__':
    print_hi('PyCharm')