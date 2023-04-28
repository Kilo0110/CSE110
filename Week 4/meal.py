from decimal import Decimal
import random
# Compute the price of a meal as follows by asking for the price of child and adult meals, the number of each, and then the sales tax rate. Use these values to determine the total price of the meal. Then, ask for the payment amount and compute the amount of change to give back to the customer.

# Keep in mind that some of these values are floating point numbers (they can have decimals) and some of them are integers (whole numbers).


# The price of a child's meal (floating point)
priceOfChildMeal = float(input('The price of a child\'s meal: '))

# The price of an adult's meal(floating point)
priceOfAdultMeal = float(input('The price of an adult\'s meal: '))

# The number of children(integer)
numberOfChildren = int(input('The number of children is: '))

# The number of adults(integer)
numberOfAdults = int(input('The number of adults: '))

# The sales tax rate(floating point)
salesTaxRate = float(input('The sales tax rate is: '))


# Determine the meal's subtotal (before adding sales tax) by multiplying the number of children by the price of their meal, and multiplying the number of adults by the price of their meal and adding those two values together.
childrenMealSubTotal = priceOfChildMeal * numberOfChildren
adultsMealSubTotal = priceOfAdultMeal * numberOfAdults

# Add childrenMealSubTotal and adultsMealSubTotal and convert to decimal
subtotalDecimal = Decimal(childrenMealSubTotal + adultsMealSubTotal)

# Convert that decimal subtotal to a decimal with 2 places
subtotal = subtotalDecimal.quantize(Decimal('0.00'))

# Randomly generate a percentage discount
percentageDiscount = random.randrange(0, 101, 1)

print(f'\n You\'ve been awarded a special discount of {percentageDiscount}% by our systems. Enter the one-time code DISCOUNT{percentageDiscount} to redeem your discount')

inputedDiscountCode = input('\n Enter special one-time code: ')

# Checks if the user enter the discount code and applies the discount if true or not if false
if inputedDiscountCode == 'DISCOUNT' + str(percentageDiscount):
  # Calculate the discount on the subtotal
  discountOnSubtotal = (percentageDiscount * subtotal) / 100

  # Apply the discount by subtracting the discount from the subtotal to get the total before tax
  totalBeforeTax = subtotal - discountOnSubtotal

  # Calculate the tax on the total
  taxOnTotal = (salesTaxRate * float(totalBeforeTax)) / 100

  # Apply the tax by adding the taxOnTotal to the totalBeforeTax
  totalPayableFee = float(totalBeforeTax) + taxOnTotal

  # Display the subtotal.
  print(f'\n Your subtotal is: ${subtotal}')

  # Display the percentage discount
  print(f'\n Your discount is: ${discountOnSubtotal} at {percentageDiscount}% discount')

  # Display the tax
  print(f'\n Your tax is: ${taxOnTotal:.2f} at {salesTaxRate}% tax')

  # Display the total fee after tax
  print(f'\n Your total before tax is: ${totalBeforeTax:.2f}')

  # Display the total fee after tax
  print(f'\n Your total after tax is: ${totalPayableFee:.2f}')
else:
  totalBeforeTax = subtotal

  # Calculate the tax on the total
  taxOnTotal = (salesTaxRate * float(totalBeforeTax)) / 100

  # Apply the tax by adding the taxOnTotal to the totalBeforeTax
  totalPayableFee = float(totalBeforeTax) + taxOnTotal

  # Display the subtotal.
  print(f'\n Your subtotal is: ${subtotal}')

  # Display the tax
  print(f'\n Your tax is: ${taxOnTotal:.2f} at {salesTaxRate}% tax')

  # Display the total fee before tax
  print(f'\n Your total before tax is: ${totalBeforeTax:.2f}')

  # Display the total fee after tax
  print(f'\n Your total after tax is: ${totalPayableFee:.2f}')

paymentAmount = float(input('\n How much will you pay to complete this transaction?: '))

change = paymentAmount - totalPayableFee

if change < 0:
  print(f'\n You still owe us ${change:.2f}')
else:
  print(f'\n Your change is ${change:.2f}')
