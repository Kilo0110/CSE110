from os import system


def convert_to_fahrenheit(temperature):
  """
  Purpose: Converts the input temperature value to its equivalent in Fahrenheit
  """
  return ((temperature * 1.8) + 32)
# end def

def calculate_windchill(temperature, wind_speed):
  """
  Purpose: Converts the input temperature value to its equivalent in Fahrenheit
  """
  return round(35.74 + (0.6215 * int(temperature)) - (35.75 * (wind_speed ** 0.16)) + (0.4275 * int(temperature) * (wind_speed ** 0.16)), 2)
# end def

def print_windchill(temperature):
  """
  Purpose: Converts the input temperature value to its equivalent in Fahrenheit
  """

  for wind_speed in range(5, 61, 5):
    wind_chill = calculate_windchill(temperature, wind_speed)
    print(f"At temperature of {temperature}F, and wind speed of {wind_speed}mph, the windchill is {wind_chill}F")
# end def

system('clear')


input_temperature = input("What is the temperature? ")
input_temperature_scale = input("Fahrenheit or Celsius (F/C)")

try:
    # comment: Checks if the user input is a number or if it can be safely converted to a number
    user_option = int(input_temperature)

    if input_temperature_scale.casefold() == "Fahrenheit".casefold() or input_temperature_scale.casefold() == "F".casefold():
      # try
      print_windchill(input_temperature)

    elif input_temperature_scale.casefold() == "Celsius".casefold() or input_temperature_scale.casefold() == "C".casefold():
      input_temperature = convert_to_fahrenheit(int(input_temperature))
      print_windchill(input_temperature)

    else:
      print("Invalid temperature scale")
except ValueError:
    print("Please input ONLY numbers.")
# end try

exit()



