sum_lst = []
lst = [sum_lst.append(num) for num in list(range(1000)) if num % 3 == 0 or num % 5 == 0]
print(f'Sum of list is: {sum(sum_lst)}')