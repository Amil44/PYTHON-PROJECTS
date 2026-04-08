list_divisor = []
number = 1
increment = 2

def divisor(number):
    for n in range(1, number + 1):
        if number % n == 0:
            list_divisor.append(n)

while len(list_divisor) <= 500:
    list_divisor = []
    divisor(number)

    number += increment
    increment += 1

print(f'List of divisor: {list_divisor}')
print(f'Count of divisor of number: {len(list_divisor)}')
print(f'Number: {list_divisor[-1]}')
