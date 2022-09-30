# апишите функцию update_dictionary(d, key, value), которая принимает на вход словарь dd и два числа: keykey и valuevalue.
#
# Если ключ keykey есть в словаре dd, то добавьте значение valuevalue в список, который хранится по этому ключу.
def print_hi(name):
    print(f'Hi, {name}')

def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    else:
        if 2 * key in d:
            d[2 * key].append(value)
        elif (2 * key not in d) and d.get(2 * key) == None:
            d[2 * key] = []
            d[2 * key].append(value)
        elif (2 * key not in d) and d.get(2 * key) != None:
            d[2 * key].append(value)
    return

d = {}                         # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)

if __name__ == '__main__':
    print_hi('PyCharm')