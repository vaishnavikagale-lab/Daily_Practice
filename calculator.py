while True:
    print("\nCalculator")
    print("1. Add")
    print("2. Sub")
    print("3. Mul")
    print("4. Div")
    print("5. fact")
    print("6. Exit")
    select = input("Enter your choice:")
    if select == "1":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Addition = ",a + b)
    elif select == "2":
         a = int(input("Enter first number: "))
         b = int(input("Enter second number: "))
         print("Subtraction = ",a - b)
    elif select == "3":
         a = int(input("Enter first number: "))
         b = int(input("Enter second number: "))
         print("Multiplication = ",a * b)
    elif select == "4":
          a = int(input("Enter first number: "))
          b = int(input("Enter second number: "))
          print("Division = ",a / b)
    elif select == "5":
         num = int(input("Enter the number :"))
         fact = 1
         for i in range(1,num + 1):
              fact = fact * i
              print("Factorial = ",fact)
    elif select == "6":
         print("Program terminated.")
         break
    else:
         print("Invalid choice.")