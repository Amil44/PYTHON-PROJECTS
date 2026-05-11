# Way 1 (Too Slow)
def smallest():
    i= 1
    while True:
        tf = True
        lst = list(range(1, 21))
        for n2 in lst:
            if i % n2 == 0: 
                tf = True
            else:
                tf = False
                break           
        i += 1
        if tf:
           return i-1
            
print(smallest())

# Way 2 (Faster)
import math

result = 1
for i in range(1, 21):
    result = math.lcm(result, i)

print(result)  