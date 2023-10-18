def group_by_rhyme(a):
    ans_matrix = [list()]
    ans_matrix[0].append(a[0])

    for s in a[1:]:
        ok = False
        for line in ans_matrix:
            if line[0][-2:] == s[-2:]:
                ok = True
                line.append(s)
                break
        if not ok:
            ans_matrix.append([s])

    return ans_matrix


if __name__ == "__main__":
    print(group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))
