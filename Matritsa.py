def print_hi(name):

    print(f'Hi, {name}')

a = 3

matric = [[0]*a]*a
matric[0][0] = 5
print(matric)

matric2 = [[0]*a for i in range(a)]
print(matric2)

if __name__ == '__main__':
    print_hi('PyCharm')