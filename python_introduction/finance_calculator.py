from calendar import month


monthly_income= 8000
monthly_expenses= 5000
monthly_savings= 3000
anual_interest= 0.05
time =12
savings=("monthly_savings*12+ (Monthly Savings * 12 * 0.05)" ,)

monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses

annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)
print(f"\nYour monthly savings are: ${monthly_savings:.2f}")

print(f"Your projected annual savings (with 5% interest): ${projected_savings:.2f}")


print (f"month savings is {monthly_income -monthly_expenses}", )
print (f"annual savings is {monthly_savings *12 + monthly_savings * anual_interest * time} " ,)