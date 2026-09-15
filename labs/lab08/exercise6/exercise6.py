position = input()
overtime_hours = int(input())
is_weekend = input()

if position == "Manager":
    base_rate  = 30
elif position == "Supervisor":
    base_rate = 20
elif position == "Staff":
    base_rate = 15
else:
    base_rate = 8

if overtime_hours <= 8:
    overtime_pay = (base_rate * 1.5) * overtime_hours
else:
    overtime_pay = (base_rate *  1.5 * 8) + (base_rate * 2.0) * (overtime_hours - 8)

if is_weekend == "yes":
    overtime_pay = overtime_pay + (overtime_hours * 5)

print(overtime_pay)
