def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')

a = int(input())
b = int(input())
c = int(input())
d = int(input())
for i in range(a, b+1):
    print(i, end='\t')
    for j in range(c, d+1):
        print(i * j, end='\t')
    print()

if __name__ == '__main__':
    print_hi('PyCharm')