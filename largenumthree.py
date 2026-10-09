def findLargest(a, b, c):
    a = int(input())
    b = int(input())
    c = int(input())

    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c