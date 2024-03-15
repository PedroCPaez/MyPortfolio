# T05 - Capstone Project

# This program will allow the user to access two different financial calculators:
# an INVESTMENT calculator or a BOND calculator.

import math

# Initial display
print("Investment - To calculate the amount of interest you'll earn on your investment.")
print("Bond - To calculate the amount you'll have to pay on a Home Loan.")
user_choice = input("Enter either 'Investment' or 'Bond' from the menu above to proceed: ")
user_choice = user_choice.upper()

# Validate user's choice (if INVESTMENT). And request data.
if user_choice == "INVESTMENT":
    amount_user_deposits = input("Please enter the amount of money you want to invest: ")
    interest_percentage = input("Please enter the interest rate (as percentage). Only the number: ")
    interest_percentage_divided_by_100 = int(interest_percentage) / 100
    years_to_invest = input("Please enter the number of years you plan to invest: ")
    interest = input("Which kind of interest would you like to invest on? 'Simple' or 'Compound'? ")
    interest = interest.upper()
    # Validate which kind of investment want to take, if SIMPLE. Calculate total amount to get and display.
    if interest == "SIMPLE":
        total_amount_with_interest_applied = int(amount_user_deposits) * (1 + interest_percentage_divided_by_100*int(years_to_invest))
        total_amount_with_interest_applied = round(total_amount_with_interest_applied, 2)
        print(f"The total amount you will get is {total_amount_with_interest_applied}")
    # Validate which kind of investment want to take, if COMPOUND. Calculate total amount to get and display.
    elif interest == "COMPOUND":
        total_amount_with_interest_applied = int(amount_user_deposits) * math.pow ((1 + interest_percentage_divided_by_100), int(years_to_invest))
        total_amount_with_interest_applied = round(total_amount_with_interest_applied, 2)
        print(f"The total amount you will get is {total_amount_with_interest_applied}")
    else:
        # Error message if choice entry is different than SIMPLE or COMPOUND.
        print("Invalid entry, please try again and choose 'SIMPLE' or 'COMPOUND'.")
# Validate user's choice (if BOND). Request data, calculate monthly payment and display.
elif user_choice == "BOND":
    present_house_value = float(input("Please enter the present value of the house: "))
    interest_rate = float(input("Please enter the annual interest rate (as percentage). Only the number: "))
    interest_percentage = interest_rate / 100
    monthly_interest_rate = interest_percentage / 12
    number_of_months_to_repay = int(input("Please enter the number of months you plan to take to repay the bond: "))
    repayment = (monthly_interest_rate * present_house_value) / (1 - (1 + monthly_interest_rate) ** (-number_of_months_to_repay))
    repayment = round(repayment, 2)
    print(f"The total amount you have to repay monthly is: {repayment}")
else:
    # Error message if choice entry is different than INVESTMENT or BOND.
    print("Invalid entry, please try again and choose 'INVESTMENT' or 'BOND'.")
