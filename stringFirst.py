def print_hi(name):

    print(f'Hi, {name}')

a = input()
G=a.upper().count('G'.upper())
C=a.upper().count('C'.upper())
sum=G+C
conclusion=sum/len(a)*100
print(conclusion)

if __name__ == '__main__':
    print_hi('PyCharm')