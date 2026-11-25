def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Exit")

ch = int(input("Enter your choice : "))

if ch == 1:
    print("Addition = ",add(a,b))
elif ch == 2:
    print("Subtraction = ",sub(a,b))
elif ch == 3:
    print("Multiplication = ",mul(a,b))
elif ch == 4:
    print("Division = ",div(a,b))
elif ch == 5:
    print("Program terminated")
else:
    print("Invalid choice")

