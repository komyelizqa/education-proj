def print_hi(name):
    print(f'Hi, {name}')

m = int(input())
t2 = m**2
while m != 0:
    t = (int(input()))
    m += t
    t2 += t**2
print(t2)
a = [0 for i in range(5)]
print(a)

my_list = list(map(int, input().split()))
print(777 in my_list)



if __name__ == '__main__':
    print_hi('PyCharm')