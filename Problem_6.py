# Way 1
def sum_of_squares(number):
    sum1 = 0
    for num1 in range(1, number + 1):
        sum1 += num1 ** 2

    return sum1

def squares_of_sum(number):
    sum1 = 0
    for num1 in range(1, number + 1):
        sum1 += num1

    return sum1 ** 2

def substaction():
    res1 = sum_of_squares(100)
    res2 = squares_of_sum(100)
    return f'Answer: {res2 - res1}'


print(substaction())



# Way 2
squares_of_sum = sum(list(map(lambda x: x, list(range(1,101))))) ** 2
sum_of_squares = sum(list(map(lambda x: x**2, list(range(1,101)))))
print(squares_of_sum - sum_of_squares)
