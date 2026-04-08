even_valued = [2]

def fibonacci():
    f1 = 1
    f2 = 2
    f3 = 0

    while f3 < 4000000:
        f3 = f1 + f2
        f1 = f2
        f2 = f3

        if f3 % 2 == 0: even_valued.append(f3)

    return f'Sum of Even_Valued: {sum(even_valued)}'

print(fibonacci())