summ = 0

# max = d × (9^5)
for num in range(2, 5*(9**5)):
    if num == sum(int(x)**5 for x in str(num)):
        summ += num

print(summ)
