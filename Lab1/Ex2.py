vowels = 'aeiou'
string = input("String: ")

counter = 0
for character in string:
    if character in vowels:
        counter = counter + 1

print(f"The number of vowels is: {counter}")