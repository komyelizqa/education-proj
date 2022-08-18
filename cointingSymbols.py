def print_hi(name):

    print(f'Hi, {name}')

s = input() + ' '
count = 1
for i in range(1, len(s)):
    if s[i - 1] == s[i]:
        count += 1
    else:
        print(s[i - 1] + str(count), end='')
        count = 1

        if __name__ == '__main__':
            print_hi('PyCharm')