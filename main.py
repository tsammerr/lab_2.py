number_1 = int(input('1 number -> '))
number_2 = int(input('2 number -> '))

while number_1 <= number_2:
    print(f'number = {number_1%2}')
    number_1 += 2