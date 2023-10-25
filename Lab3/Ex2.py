def freq(s):
    f = {}
    for letter in s:
        if letter in f:
            f[letter] += 1
        else:
            f[letter] = 1

    return f


if __name__ == "__main__":
    print(freq("Ana has apples"))
