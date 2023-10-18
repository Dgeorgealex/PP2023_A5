def list_from_input(string):
    return [int(x) for x in string.split(' ')]


def my_sets(a, b):
    copy_a = list(sorted(set(a)))
    copy_b = list(sorted(set(b)))

    print(copy_a)
    print(copy_b)

    intersection = []
    union = []
    index_a = 0
    index_b = 0

    while index_a < len(copy_a) and index_b < len(copy_b):
        if copy_a[index_a] == copy_b[index_b]:
            intersection.append(copy_a[index_a])
            to_add = copy_a[index_a]
            index_a += 1
            index_b += 1

        elif copy_a[index_a] < copy_b[index_b]:
            to_add = copy_a[index_a]
            index_a += 1

        else:
            to_add = copy_b[index_b]
            index_b += 1

        if len(union) == 0 or (len(union) > 0 and union[-1] != to_add):
            union.append(to_add)

    while index_a < len(copy_a):
        if len(union) == 0 or (len(union) > 0 and union[-1] != copy_a[index_a]):
            union.append(copy_a[index_a])
        index_a += 1

    while index_b < len(copy_b):
        if len(union) == 0 or (len(union) > 0 and union[-1] != copy_b[index_b]):
            union.append(copy_b[index_b])
        index_b += 1

    a_minus_b = list(filter(lambda x: x not in copy_b, union))
    b_minus_a = list(filter(lambda x: x not in copy_a, union))

    return intersection, union, a_minus_b, b_minus_a


if __name__ == "__main__":
    a = list_from_input(input())
    b = list_from_input(input())
    print(my_sets(a, b))