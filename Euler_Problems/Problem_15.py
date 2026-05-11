def routes(N):
    factorial_2N = 1
    factorial_N = 1

    for i in range(1, N + 1):
        factorial_N *= i

    for i in range(1, 2*N + 1):
        factorial_2N *= i

    return f'Answer: {factorial_2N // (factorial_N * factorial_N)}'

grid_N = int(input('N x N: '))
print(routes(grid_N))
