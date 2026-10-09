def sumOfN(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total
n = int(input("Enter the number: "))
print(sumOfN(n))