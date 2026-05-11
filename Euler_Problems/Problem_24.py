number = '012'
# all_posb = ''

def iteration(len_number):
    f = 1
    for i in range(1, len(number) + 1):
        f *= i
    return f

def slide_digit(main_digit):
    save_digit = number[0]
    number.replace(number[0], main_digit)
    number.replace(number[int(main_digit)], save_digit)
    return number


for _ in range(1, iteration(len(number)) + 1):
    all_posb = ''

    for i in range(len(number)):
        main_digit = number[i]
            
        k = number[i + 1:]
        all_posb += main_digit + k
        slide_digit(main_digit)
    print(all_posb)
                
