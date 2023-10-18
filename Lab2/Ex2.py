def get_primes_from_list(l):
    primes = []
    for number in l:
        if number == 0 or number == 1:
            continue
        divisor = 2
        ok = True
        while divisor * divisor <= number:
            if number % divisor == 0:
                ok = False
                break
            divisor = divisor + 1
        if ok:
            primes.append(number)

    return primes


if __name__ == "__main__":
    string = input()
    list_of_strings = string.split(' ')
    my_list = [int(x) for x in list_of_strings]
    my_prime_list = get_primes_from_list(my_list)
    print(my_prime_list)
