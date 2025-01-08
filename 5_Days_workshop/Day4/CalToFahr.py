# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Input from the user
celsius = float(input("Enter the temperature in Celsius: "))

# Convert to Fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)

# Print the result
print(f"The temperature in Fahrenheit is: {fahrenheit:.2f}°F")
