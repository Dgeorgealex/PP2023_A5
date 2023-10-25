def loop(mapping):
    ans_list = []
    current_value = mapping['start']
    while True:
        ans_list.append(current_value)
        current_value = mapping[current_value]
        if current_value in ans_list:
            break

    return ans_list


if __name__ == "__main__":
    print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
