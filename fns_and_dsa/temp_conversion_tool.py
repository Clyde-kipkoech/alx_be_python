
FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5


def  convert_to_celsius(fahrenheit) :

    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius) :
    
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Prompt user for temperature
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)

        # Prompt for temperature unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {result}°F")
        elif unit == 'F':
            result = convert_to_celsius(temperature)
            print(f"{temperature}°F is {result}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
