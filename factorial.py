def print_hi(name):
    print(f'Hi, {name}')

m = int(input())
list = []
for i in range(m+1):
    count = 0
    while count < i+1:
        list.append(i+1)
        count += 1
        if m == len(list):
            for j in list:
                print(j, end=' ')
            break

if __name__ == '__main__':
    print_hi('PyCharm')