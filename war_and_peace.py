def print_hi(name):
    print(f'Hi, {name}')


def f(x):
    return x**3

l = int(input())
list1=[]
list2=[]
dic={}
for i in range(l):
    x = int(input())
    if x in dic:
        print(dic[x])
    else:
        dic[x] = f(x)
        print(dic[x])

# a=[int(input()) for i in range(int(input()))]
# b={x:f(x) for x in set(a)}
# for i in a:
#     print(b[i]


if __name__ == '__main__':
    print_hi('PyCharm')