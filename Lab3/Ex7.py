def my_sets_operations(*sets):
    ans_dict = {}
    for i, my_set1 in enumerate(sets):
        for j, my_set2 in enumerate(sets):
            if i < j:
                # reunion
                ans_dict[f"{my_set1} | {my_set2}"] = my_set1 | my_set2

                # intersection
                ans_dict[f"{my_set1} & {my_set2}"] = my_set1 & my_set2

                # a-b
                ans_dict[f"{my_set1} - {my_set2}"] = my_set1 - my_set2

                # b-a
                ans_dict[f"{my_set2} - {my_set1}"] = my_set2 - my_set1

    return ans_dict


if __name__ == "__main__":
    print(my_sets_operations({1, 2}, {2, 3}))
