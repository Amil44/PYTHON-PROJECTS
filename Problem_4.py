# Way 1
largest = 0

for num1 in range(100, 1000):
    for num2 in range(100, 1000):
        if num1 * num2 == int(str(num1 * num2)[::-1]):
            if largest <  num1 * num2: 
                largest =  num1 * num2

print(largest)




# Way 2
l = [[x * y for x in range(100, 1000) if x * y == int(str(x * y)[::-1])] for y in range(100, 1000)]
print(*max(*l))
