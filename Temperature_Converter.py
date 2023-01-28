def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

while True:
    # Get user input for temperature and unit
    temp = float(input("Enter a temperature: "))
    unit = input("Enter the unit of the temperature (C or F): ").upper()
    
    # Check the unit and convert the temperature
    if unit == "C":
        print(f"{temp} degree Celsius is equivalent to {celsius_to_fahrenheit(temp)} degree Fahrenheit")
    elif unit == "F":
        print(f"{temp} degree Fahrenheit is equivalent to {fahrenheit_to_celsius(temp)} degree Celsius")
    else:
        print("Invalid unit entered. Please enter either 'C' for Celsius or 'F' for Fahrenheit.")
