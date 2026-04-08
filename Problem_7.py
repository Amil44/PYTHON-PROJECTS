def is_prime(number):
    for i in range(2, int(number**0.5) + 1 ):
        if number % i == 0:
            return False
    return number

indexx = 1
number = 2

while indexx != 10001:
    number += 1

    while is_prime(number) == False:
        number += 1
    indexx += 1

print(number)


