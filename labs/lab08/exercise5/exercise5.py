main_course = input()
drink = input()
dessert = input()

if main_course == "Chicken":
    final_bill = 10
elif main_course == "Beef":
    final_bill = 12
else:
    final_bill = 11

if drink == "Soft Drink":
    final_bill = final_bill + 2
else:
    final_bill = final_bill + 3

if dessert == "Ice Cream":
    final_bill = final_bill + 4
else:
    final_bill = final_bill + 5

final_bill = final_bill * 1.1

print(f"{final_bill:.2f}")
