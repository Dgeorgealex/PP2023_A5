def number_of_bits(number):
    counter = 0
    while number != 0:
        number = number & (number - 1)
        counter = counter + 1
    return counter


nr = int(input("Number: "))
print(f"The number of set bits is {number_of_bits(nr)}")
