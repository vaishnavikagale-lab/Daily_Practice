n = int(input("Enter the number: "))
if n >= 0 and str(n) == str(n)[::-1]:
    print(True)
else:
    print(False)