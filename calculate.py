def calculate(a: int, b: int, op: str):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Division by zero"
        return round(a / b, 2)
    elif op == "//":
        if b == 0:
            return "Division by zero"
        return a // b
    elif op == "%":
        if b == 0:
            return "Division by zero"
        return a % b
    elif op == "**":
        return a ** b