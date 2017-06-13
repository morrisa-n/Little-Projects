# Friendly Little Temperature Converter
# A quick little script that converts from Fahrenheit to Celsius, or from Celsius to Fahrenheit

a = '\u00b0'

print("""Hello, I am your friendly temperature converter, here to
change temperatures from Fahrenheit to Celsius for you,
or vice versa.""")

temp_type = input("Which would you like to convert from, Fahrenheit or Celsius? (Enter full name or first letter) ").lower()
if temp_type == "fahrenheit" or temp_type == "f":
    temp = float(input("Okay. And what is the temperature you'd like to convert to Celsius? (Numbers only, please) "))
    final = (temp - 32.0) * 5.0 / 9.0
    print("{0}{1}F is {2}{3}C.".format(temp, a, final, a))
else:
    temp = float(input("Okay. And what is the temperature you'd like to convert to Fahrenheit? (Numbers only, please) "))
    final = (temp * (9 / 5)) + 32
    print("{0}{1}C is {2}{3}F.".format(temp, a, final, a))
print("Have a wonderful day. :)")
