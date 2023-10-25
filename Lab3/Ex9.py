def my_function(*args, **kwargs):
    nr = 0
    for value in args:
        if value in kwargs.values():
            nr += 1

    return nr


if __name__ == "__main__":
    print(my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5))
