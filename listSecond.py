def print_hi(name):

    print(f'Hi, {name}')

numbersOfList = [int(i) for i in input().split()]
numbersOfList.sort()
final = []
for k in numbersOfList:
    if numbersOfList.count(k) <= 1:
        continue
    final.append(k)
    while numbersOfList.count(k) > 1:
        numbersOfList.remove(k)
for x in final:
    print(x, end=' ')

if __name__ == '__main__':
    print_hi('PyCharm')