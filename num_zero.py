def number_to_zero(num):
    steps = 0
    while num > 0:
        if num % 2 == 0:
           num = num // 2 
        else:
            num = num - 1
        steps = steps + 1
        return steps
num = int(input("Enter the number:"))
print(number_to_zero(num))