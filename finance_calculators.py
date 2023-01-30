import math
#Create a program that allows the user to access two different financial calculators: investment or bond.

#User to enter if they want investment or bond calc. Any variation of either word will be recognised by making it lowercase.
#Provide error message if invalid input
calc_type = input("Please choose either 'investment' or 'bond' calculator: ")
calc_type = calc_type.lower()
if calc_type == "investment":
    print("\nYou have chosen the investment calculator")
elif calc_type == "bond":
    print("\nYou have chosen the bond calculator")
else:
    print("\nInvalid input. Please try again.")

#If investment, ask user to input variables needed to calculate simple or compound interest.

if calc_type == "investment":
    deposit = float(input("\nPlease enter the amount of money you will deposit: "))
    deposit = round(deposit, 2)
    invest_interest_rate = float(input("\nPlease enter the anticipated annual interest rate: "))
    invest_interest_rate = round(invest_interest_rate, 2)
    invest_interest_rate = invest_interest_rate / 100
    investment_years = int(input("\nPlease enter the number of years you plan to invest: "))
    interest = input("\nPlease choose 'simple' or 'compound' interest: ")
    interest = interest.lower()

# Use interest formula calculation to find total amount after simple interest applied
    if interest == "simple":
        total_simple = deposit * (1 + invest_interest_rate * investment_years)
        total_simple = round(total_simple, 2)
        print(f"\nYour final investment total with simple interest is: £{total_simple}")

# Use interest formula calculation to find total amount after compound interest applied.
# Include error message if invalid input.
    elif interest == "compound":
        total_compound = deposit * math.pow((1 + invest_interest_rate),investment_years)
        total_compound = round(total_compound, 2)
        print(f"\nYour final investment total with compound interest is: £{total_compound}")
    else:
        print("\nInvalid input. Please try .")

#If bond, ask user to enter variables needed to calculate bond repaymentsper month.
if calc_type == "bond":
    house_value = float(input("\nPlease enter the value of your house: "))
    house_value = round(house_value)
    bond_interest_rate = float(input("\nPlease enter the anticipated annual interest rate: "))
    bond_interest_rate = round(bond_interest_rate, 2)
    bond_interest_rate = bond_interest_rate / 100
    bond_annual_interest_rate = bond_interest_rate / 12
    bond_months = int(input("\nPlease enter the number of months you plan to take to repay the bond: "))
    bond_months = round(bond_months)
    total_bond = (bond_annual_interest_rate * house_value) / (1 - (1 + bond_annual_interest_rate) ** (- bond_months))
    total_bond = round(total_bond,2)
    print(f"\n Your monthly bond repayment on a home loan is: £{total_bond}")


