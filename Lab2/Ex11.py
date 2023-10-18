def sort_string_tuples(a):
    a.sort(key=lambda x: x[1][2])
    return a


if __name__ == "__main__":
    ans = sort_string_tuples([('abc', 'bcd'), ('abc', 'zza')])
    print(ans)