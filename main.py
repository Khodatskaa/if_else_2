num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 == num2:
    print("Numbers are equal")
else:
    if num1 < num2:
        smaller_num = num1
        larger_num = num2
    else:
        smaller_num = num2
        larger_num = num1

    print(f"Numbers in rising order: {smaller_num}, {larger_num}")
