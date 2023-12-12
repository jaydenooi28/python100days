print("Thank you for choosing Python Pizza Deliveries!")
size = input('Size = ') # What size pizza do you want? S, M, or L
add_pepperoni = input('Pep = ') # Do you want pepperoni? Y or N
extra_cheese = input('Chees = ') # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇


# Small Pizza
if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
# Medium Pizza
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1


# Large Pizza
else:
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1

# Print the final bill
print (f'Your final bill is: ${bill}.')



