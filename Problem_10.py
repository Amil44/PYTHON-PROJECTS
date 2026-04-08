lst = []

def prime(number):
    for n in range(2, int(number**0.5) + 1):
        if number % n == 0:
            return False
        
    lst.append(number)

for num in range(2, 2000000):
    prime(num)

print(sum(lst))

    

