def compare_dict(a, b):
    if not isinstance(a, dict) or not isinstance(b, dict):
        return False

    if len(a) != len(b):
        return False

    for key_a in a:
        if key_a not in b:
            return False
        if not compare_element(a[key_a], b[key_a]):
            return False
    return True


def compare_set(a, b):
    if not isinstance(a, set) or not isinstance(b, set):
        return False

    if len(a) != len(b):
        return False

    for in_a in a:
        if in_a not in b:
            return False

    return True


def compare_list_tuple(a, b):  # kinda?
    if type(a) != type(b):
        return False

    if len(a) != len(b):
        return False

    for i in range(len(a)):
        if not compare_element(a[i], b[i]):
            return False

    return True


def compare_element(a, b):
    if type(a) != type(b):
        return False

    if isinstance(a, dict):
        return compare_dict(a, b)

    if isinstance(a, list) or isinstance(a, tuple):
        return compare_list_tuple(a, b)

    if isinstance(a, set):
        return compare_set(a, b)

    return a == b


if __name__ == "__main__":
    dict1 = {
        'name': 'John',
        'age': 30,
        'interests': ['reading', 'hiking', 'music'],
        'address': {
            'street': '123 Main St',
            'city': 'Anytown',
            'zipcode': '12345'
        },
        'friends': {'Alice', 'Bob', 'Charlie'}
    }
    dict2 = {
        'name': 'John',
        'age': 30,
        'interests': ['reading', 'hiking', 'music'],
        'address': {
            'street': '123 Main St',
            'city': 'Anytown',
            'zipcode': '12345'
        },
        'friends': {'Alice', 'Bob', 'Charlie'}
    }
    print(compare_dict(dict1, dict2))
