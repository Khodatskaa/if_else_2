import math

d = float(input('Enter diameter: '))

print('Choose an operation')
print('1. Circle perimeter')
print('2. Circle area')
choice = input('Enter operation number(1/2): ')

if choice == "1":
    r = d / 2
    perimeter = 2 * math.pi * r
    print(perimeter)
elif choice == "2":
    r = d / 2
    area = math.pi * r * r
    print(area)
else:
    print("Unknown operation number")