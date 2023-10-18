def get_palindromes(nr_list):
    nr_pal = 0
    max_pal = 0
    for nr in nr_list:
        rev = 0
        co = nr
        while co != 0:
            rev = rev*10 + co % 10
            co = co // 10

        if rev == nr:
            max_pal = max(max_pal, nr)
            nr_pal += 1

    return nr_pal, max_pal


if __name__ == "__main__":
    print(get_palindromes([1, 2, 12, 31, 313]))
