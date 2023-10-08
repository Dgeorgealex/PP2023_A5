# Find The greatest common divisor of multiple numbers read from the console.

def cmmdc(a, b):
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b

    return b


input_string = input("List: \n")

input_words = input_string.split()

number_list = []

for word in input_words:
    number = int(word)
    number_list.append(number)

gcd = number_list[0]
for number in number_list:
    gcd = cmmdc(gcd, number)

print(f"The gcd is: {gcd}")
