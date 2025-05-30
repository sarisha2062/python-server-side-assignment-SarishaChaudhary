def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact(num - 1)
num= int(input(" enter the number to claculate factorial : "))
if num < 0:
    print("Please Enter positive number.")
else:
    n = fact(num)
    print(f"The factorial of {num} is {n}")