def get_number_from_text(text):
    ans = ''
    for i in range(len(text)):
        if text[i].isnumeric():
            j = i
            while j < len(text) and text[j].isnumeric():
                ans = ans + text[j]
                j = j + 1
            return ans

    return ans


string = input()
print(f"The first number in the string is {get_number_from_text(string)}")