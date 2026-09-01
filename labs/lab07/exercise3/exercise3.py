name = input()
price = float(input())
quantity = int(input())
member_answer = input()

order_total = price * quantity

if order_total >= 100 :
    free_shipping = "True"
elif order_total > 0 :
    free_shipping = "False"

if member_answer == "yes":
    is_member = True
elif member_answer == "no":
    is_member = False

print(name.upper())
print(order_total)
print(free_shipping)
print(is_member)
