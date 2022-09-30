def print_hi(name):

    print(f'Hi, {name}')

with open(r'C:\Users\lizro\Downloads\dataset_3363_2.txt', 'r') as inf:
    s1 = inf.readline()
    import re
    g = re.findall(r'\d+', s1)
    f = [i for i in s1 if i.isalpha()]
    h = "".join([int(i)*j for i, j in zip(g, f)])
    with open(r'C:\\Users\\lizro\\Downloads\\dataset_3363_2.txt', 'w') as inf:
        inf.write(h)

if __name__ == '__main__':
    print_hi('PyCharm')