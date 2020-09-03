# Author: Abigail Bowen aeb6095@psu.edu
# Collaborator: Ethan Wertz evw5316@psu.edu
# Collaborator: David Oke doo5136@psu.edu
# Collaborator: Kelly McVeigh kam7563@psu.edu

temperature = input("Enter temperature: ")
unit = input("Enter unit in F/f or C/c: ")
temperature = float(temperature)
if unit == "F" or unit == "f":
  f = (temperature - 32) * 5/9
  print(f"{temperature}° in Fahrenheit is equivalent to {f}° Celsius.")

elif unit == "C" or unit == "c":
  c = (temperature * 9/5) + 32
  print(f"{temperature}° in Celsius is equivalent to {c}° Fahrenheit.")
else:
  print(f"Invalid unit({unit}).")
