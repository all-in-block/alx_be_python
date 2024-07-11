FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius= (fahrenheit - 32)* FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {celsius}°C")

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius}°C is {fahrenheit}°F")
def main():
        try:
         temperature = float(input("Enter the temperature to convert: "))
         temp_type = input("is the temperature in Celsius or Fahrenheit (C/F) ")
         if temp_type == "C":
            convert_to_fahrenheit(temperature)
         elif temp_type == "F":
            convert_to_celsius(temperature)
         else:
            print("choose C or F")
        except ValueError:
           print("enter a valid temperature")

main()