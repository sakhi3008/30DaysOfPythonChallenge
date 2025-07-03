#Challenge -  Build a temperature converter CLI tool

import argparse

def temperature_converter(value, from_unit, to_unit):
    # first convert input to celcius
    if from_unit == "C":
        celcius = value
    elif from_unit == "F":
        celcius = (value - 32) * 5/9
    elif from_unit == "K":
        celcius = value - 273.15
    else:
        raise ValueError("Unsupported from_unit. Use 'C', 'F', or 'K'.")
    
    #convert celcius to target unit
    if to_unit =="C":
        return celcius
    elif to_unit == "F":
        return (celcius * 9/5) + 32
    elif to_unit == "K":    
        return celcius + 273.15
    else:
        raise ValueError("Unsupported to_unit. Use 'C', 'F', or 'K'.")
    

#Setup argument parser
parser = argparse.ArgumentParser(description = "Convert temperature between Celsius, Fahrenheit, and Kelvin.")
parser.add_argument("value", type = float, help = "Temperature value to convert")
parser.add_argument("from_unit", type = str, choices = ["C", "F", "K"], help = "Unit to convert from: C, F, or K")
parser.add_argument("to_unit", type = str, choices = ["C", "F", "K"], help = "Unit to convert to: C, F, or K")

args = parser.parse_args()

result = temperature_converter(args.value, args.from_unit.upper(), args.to_unit.upper())
print(f"{args.value}{args.from_unit.upper()} is equal to {round(result, 2)}{args.to_unit.upper()}")

