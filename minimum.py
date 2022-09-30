def print_hi(name):
    print(f'Hi, {name}')

a = [int(i) for i in input().split()]
m = a[0]
for j in a:
    if m>j:
        m = j
print(m)
if __name__ == '__main__':
    print_hi('PyCharm')