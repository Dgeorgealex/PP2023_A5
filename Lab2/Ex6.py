def frequent_items(x, *args):
    ans = []
    f = {}
    for l in args:
        for el in l:
            if el in f:
                f[el] += 1
            else:
                f[el] = 1

    for el in f.items():
        if el[1] == x:
            ans.append(el[0])

    return ans


if __name__ == "__main__":
    print(frequent_items(2, [1,2,3],[2,3,4],[4,5,6], [4,1, "test"]))



