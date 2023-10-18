def get_fibo(n):
    fibo = [0] * n
    fibo[0] = 1
    if n == 1:
        return fibo

    fibo[1] = 1
    if n == 2:
        return fibo

    for i in range(n - 2):
        fibo[i + 2] = fibo[i + 1] + fibo[i]

    return fibo


if __name__ == '__main__':
    n = int(input())
    fibo = get_fibo(n)
    print(fibo)
