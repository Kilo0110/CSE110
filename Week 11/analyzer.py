import csv
from os import system
from collections import defaultdict
from decimal import Decimal


system('clear')


def convert_to_decimal(number):
    """
    Purpose: Convert a number to decimal
    """
    initial_value = float(number)
    formatted_value = Decimal(initial_value).quantize(Decimal('0.00'))
    return formatted_value
# end def


data = defaultdict(list)

with open('life-expectancy.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # print(row)
        for key, value in row.items():
            data[key].append(value)

# Find the year and country with the lowest life expectancy
min_overall_expectancy = min(data['Life expectancy (years)'])
min_index = data['Life expectancy (years)'].index(
    min(data['Life expectancy (years)']))
min_year = data['Year'][min_index]
min_country = data['Entity'][min_index]

# Find the year and country with the lowest life expectancy
max_overall_expectancy = max(data['Life expectancy (years)'])
max_index = data['Life expectancy (years)'].index(
    max(data['Life expectancy (years)']))
max_year = data['Year'][max_index]
max_country = data['Entity'][max_index]

print(
    f"The overall max life expectancy is: {convert_to_decimal(max_overall_expectancy)} from {max_country} in {max_year}")

print(
    f"The overall min life expectancy is: {convert_to_decimal(min_overall_expectancy)} from {min_country} in {min_year}")

# Allow the user to input a year and find the average life expectancy for that year
year_of_interest = input("Enter the year of interest: ")
sum_life_expectancy = 0
count = 0

print()
print(f"For the year {year_of_interest}:")

for i in range(len(data['Year'])):
    if data['Year'][i] == year_of_interest:
        sum_life_expectancy += float(data['Life expectancy (years)'][i])
        count += 1
if count > 0:
    avg_life_expectancy = sum_life_expectancy / count
    print(
        f"The average life expectancy across all countries was {convert_to_decimal(avg_life_expectancy)}.")
else:
    print(f"No data available for year {year_of_interest}.")

# Find the country with the minimum and maximum life expectancies for the user-inputted year
min_life_expectancy = float('inf')
max_life_expectancy = float('-inf')
min_country = ""
max_country = ""


for i in range(len(data['Year'])):
    if data['Year'][i] == year_of_interest:
        life_expectancy = float(data['Life expectancy (years)'][i])
        if life_expectancy < min_life_expectancy:
            min_life_expectancy = life_expectancy
            min_country = data['Entity'][i]
        if life_expectancy > max_life_expectancy:
            max_life_expectancy = life_expectancy
            max_country = data['Entity'][i]
if min_country and max_country:
    print(
        f"The max life expectancy was in {max_country} with {convert_to_decimal(max_life_expectancy)}.")
    print(
        f"The min life expectancy was in {min_country} with {convert_to_decimal(min_life_expectancy)}.")
else:
    print(f"No data available for year {year_of_interest}.")
