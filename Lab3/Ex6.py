def unique_and_not(my_list):
    my_set = set(my_list)
    # number of duplicated elements
    return len(my_set), len(my_list) - len(my_set)


def unique_and_not_two(my_list):
    my_unique_set = set()
    my_not_unique_set = set()
    for item in my_list:
        if item in my_not_unique_set:
            continue

        if item in my_unique_set:
            my_not_unique_set.add(item)
            my_unique_set.remove(item)
        else:
            my_unique_set.add(item)

    return len(my_unique_set), len(my_not_unique_set)


if __name__ == "__main__":
    print(unique_and_not([1, 2, 2, 3, 4, 4, 5]))
    print(unique_and_not_two([1, 2, 2, 3, 4, 4, 5]))
