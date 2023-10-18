def get_list_elements(*args):
    max_len = max(len(x) for x in args)
    ans_list = [tuple()] * max_len
    for my_list in args:
        for index, element in enumerate(my_list):
            ans_list[index] += (element,)

    return ans_list


if __name__ == "__main__":
    print(get_list_elements([1, 2, 3], [5, 6, 7], ["a", "b", "c"]))