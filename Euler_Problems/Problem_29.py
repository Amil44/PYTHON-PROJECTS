lst_num = []

for a in range(2, 101):
    for b in range(2, 101):
        num = a ** b
        lst_num.append(num)

print(len(set(lst_num)))

