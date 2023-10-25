def validate_dict(rules, my_dict):
    checked = set()
    for rule in rules:
        if rule[0] not in my_dict:
            return False

        s = my_dict[rule[0]]

        if len(rule[1]) != 0 and (len(rule[1]) > len(s) or rule[1] != s[:len(rule[1])]):
            return False

        if len(rule[3]) != 0 and (len(rule[3]) > len(s) or rule[3] != s[-len(rule[1]):]):
            return False

        if len(rule[2]) != 0 and (len(rule[2]) > len(s) - 2 or rule[2] not in s[1:-1]):
            return False

        checked.add(rule[0])

    # if checked != rules.keys():
    #   return False

    return True


if __name__ == "__main__":
    s = {("key1", "", "inside", ""), ("key", "this", "this", "valid")}
    d = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
    print(validate_dict(s, d))
