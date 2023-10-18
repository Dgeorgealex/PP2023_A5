def get_letters(x=1, strings=None, flag=True):
    list_of_list = []
    for string in strings:
        l = []
        for ch in string:
            if (ord(ch) % x == 0) == flag:
                l.append(ch)

        list_of_list.append(l)

    return list_of_list


if __name__ == "__main__":
    print(get_letters(2, ["test", "hello", "lab002"], False))
