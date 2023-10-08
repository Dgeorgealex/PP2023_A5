string = input("Input UpperCamelCase: ")

snake_case = string[0].lower()

for character in string[1:]:
    if character.isupper():
        snake_case += '_'

    snake_case += character.lower()

print(snake_case)
