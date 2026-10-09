def isPerfectNumber(num: int) -> bool:
    total = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            total = total + i
    return total == num 
num = int(input("Enter the number:"))
print(isPerfectNumber(num))