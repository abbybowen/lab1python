temperature = input("Enter temperature: ")
unit = input("Enter unit in F/f or C/c: ")
temperature = float(temperature)
if unit == "F" or unit == "f":
  f = (temperature - 32) * 5/9
  print(str(temperature) + "\N{DEGREE SIGN} in Fahrenheit is equivalent to " + str(f) + "\N{DEGREE SIGN} Celsius.")

elif unit == "C" or unit == "c":
  c = (temperature * 9/5) + 32
  print(str(temperature) + "\N{DEGREE SIGN} in Celsius is equivalent to " + str(c) + "\N{DEGREE SIGN} Fahrenheit.")
else:
  print(f"Invalid unit({unit}).")
