def multiplicationTable(n, limit):
    result = []

    for i in range(1, limit + 1):
        result.append(n * i)
    return result
n = int(input("Enter the number: "))
limit = int(input("Enter the limit: "))
print(multiplicationTable(n, limit))