def is_palindrome(number):
    copy_nr = number
    rev = 0
    while copy_nr > 0:
        rev = rev * 10 + copy_nr % 10
        copy_nr = int(copy_nr / 10)

    if rev == number:
        return True
    else:
        return False


nr = int(input("Number is: "))
print(is_palindrome(nr))