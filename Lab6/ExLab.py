import sys
suma = 0
try:
    for val in sys.argv[1:]:
        suma += int(val)
    print("Sum=", suma)
except:
    print("Invalid parameters")