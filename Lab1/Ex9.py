def get_most_common_chr(s):
    maximum = 0
    letter = ''
    for character in s:
        if character.isalpha():
            nr_apparitions = s.count(character.lower())
            if nr_apparitions > maximum:
                maximum = nr_apparitions
                letter = character.lower()

    print(f"The most common character is {letter} ({maximum} times)")


string = input()
get_most_common_chr(string)
