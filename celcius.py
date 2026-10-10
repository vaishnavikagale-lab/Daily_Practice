def celsius_to_fahrenheit(c: float) -> float:
    return int((c * 9 / 5) + 32)
c = float(input("Enter the celcius: "))
print(celsius_to_fahrenheit(c))