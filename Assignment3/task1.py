def factorial(num):
    if num < 2:
        return 1
    return num * factorial(num - 1)


num = int(input("Enter a number: "))
print(f"Factorial of {num} is: {factorial(num)}" if num >= 0 else "Undefined")
