sum = 0
for num in range(1, 1001):
    sum += num**num
print(f'The last ten digits of the series: {sum % 10**10}')