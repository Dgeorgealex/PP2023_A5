nr = int(input("Number: "))

counter = 0

while nr != 0:
    nr = nr & (nr - 1)
    counter = counter + 1

print(f"The number of set bits is {counter}")
