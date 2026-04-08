number = 999999
biggest_chain = {}

def odd_even(number):
    count_chain = 0

    while number != 1:
        if number % 2 == 0:
            number //= 2
            count_chain += 1
        else:
            number = number*3 + 1
            count_chain += 1

    return count_chain + 1 

while number > 1:
    biggest_chain.update({number: odd_even(number)})
    number -= 1

# print(biggest_chain)
# print(max(biggest_chain.values()))

for k, v in biggest_chain.items():
    if v == max(biggest_chain.values()):
        print(f'Number: {k} and its chain-length: {v}')