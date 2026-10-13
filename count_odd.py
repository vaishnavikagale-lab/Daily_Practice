n = abs(int(input("Enter the number: ")))
count = 0

while n > 0:
    digit = n % 10

    if digit % 2 != 0:
        count = count + 1
    n //= 10
print(count)