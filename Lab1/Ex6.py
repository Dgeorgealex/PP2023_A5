nr = int(input("Number: "))
copy_nr = nr

rev = 0

while nr > 0:
    rev = rev * 10 + nr % 10
    nr = int(nr / 10)

if rev == copy_nr:
    print(True)
else:
    print(False)
    