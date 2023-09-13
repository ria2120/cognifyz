def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Temperature Converter")
    print("---------------------")

    temperature = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit): ").upper()

    if unit == 'C':
        converted_temperature = celsius_to_fahrenheit(temperature)
        print(f"{temperature:.2f}°C is equal to {converted_temperature:.2f}°F")
    elif unit == 'F':
        converted_temperature = fahrenheit_to_celsius(temperature)
        print(f"{temperature:.2f}°F is equal to {converted_temperature:.2f}°C")
    else:
        print("Invalid unit of measurement. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()