

print("How much is your one time contribution?")
contribution = float(input())

print("How many years until you retire?")
investment_years = float(input())

print("Optional: What's your expected rate of return (eg: 0.1)?")

rate = input()

if rate == '':
    rate = 0.1
else:
    rate = float(rate)

total_earned = contribution * (1+rate)**investment_years

print ("You would earn", round(total_earned, 2), "investing this one-time contribution")

print("Optional: What's your expected withdrawl rate (eg: 0.04)?")
withdrawl_rate = input()

if withdrawl_rate == '':
    withdrawl_rate = 0.04
else:
    withdrawl_rate = float(withdrawl_rate)


yearly_surplus = withdrawl_rate * total_earned

print ("You would earn", round(yearly_surplus, 2), "a year in retirement on this one time contribution")

print("Optional: What is the rate of inflation (eg: 0.05)?")

inflation_rate = input()

if inflation_rate == '':
    inflation_rate = 0.05
else:
    inflation_rate = float(inflation_rate)

print("Optional: What is your goal retirment income in today's dollars (eg: 60,000)?")

income = input()

if income == '':
    income = 60000
else:
    income = float(income)

retirement_income = income * (1+inflation_rate)**(investment_years)
percentage_acheived = yearly_surplus/retirement_income * 100

print("Your retirement income is", round(retirement_income,2), "after inflation")
print("You are", round(percentage_acheived, 5), "percent of the way there with this one time contribution")