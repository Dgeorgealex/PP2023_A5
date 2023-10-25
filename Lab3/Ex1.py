def my_sets(a, b):
    set_a = set(a)
    set_b = set(b)
    return set_a & set_b, set_a | set_b, set_a - set_b, set_b - set_a


if __name__ == "__main__":
    a = [int(x) for x in input().split(' ')]
    b = [int(x) for x in input().split(' ')]
    print(my_sets(a, b))