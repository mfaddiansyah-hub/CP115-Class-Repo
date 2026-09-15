employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()

gross = base_salary + (overtime_hours * 35)

if (tax_status == "Single" and gross >= 5000):
    tax_rate = 0.22
elif (tax_status == "Single"):
    tax_rate = 0.18
elif (tax_status == "Married" and gross >= 6000):
    tax_rate = 0.20
elif (tax_status == "Married"):
    tax_rate = 0.15
elif (tax_status == "Head" and gross >= 5500):
    tax_rate = 0.25
else:
    tax_rate = 0.19

net_salary = gross - (gross * (tax_rate + 0.11 + 0.005))

print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")
