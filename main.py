number_1 = int(input('1 number -> '))
number_2 = int(input('2 number -> '))

if number_1 % 2 != 0:
    number_1 += 1

while number_1 <= number_2:
    print(f'number = {number_1}')
    number_1 += 2