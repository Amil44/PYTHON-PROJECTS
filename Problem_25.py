def fibonacci():
    index_1000_digit = 2
    f1 = 1
    f2 = 1
    f3 = 0

    while len(str(f3)) != 1000:
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        index_1000_digit += 1
        # print(f3)

        if len(str(f3)) == 1000:
            return f'index: {index_1000_digit}\nnumber: {f3}'
        
print(fibonacci())
        

