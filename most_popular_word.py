def print_hi(name):

    print(f'Hi, {name}')

dictionary = {}

math_values = []
physics_values = []
russian_values = []
with open(r'C:\\Users\\lizro\\Downloads\\dataset_3363_4.txt', 'r') as in_file:
    for line in in_file:
        current_line = line.strip().split(';')
        math_values.append(int(current_line[1]))
        physics_values.append(int(current_line[2]))
        russian_values.append(int(current_line[3]))
out_file = open(r'C:\\Users\\lizro\\Downloads\\Statistic.txt', 'w')
for i in range(len(math_values)):
    out_file.write(str((math_values[i] + physics_values[i] + russian_values[i]) / 3) + '\n')
if len(math_values) > 0:
    out_file.write(str(sum(math_values) / len(math_values)) + ' ' +
                   str(sum(physics_values) / len(physics_values)) + ' ' +
                   str(sum(russian_values) / len(russian_values)))
out_file.close()

if __name__ == '__main__':
    print_hi('PyCharm')