line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
x = (position[0]).lower()
y = (int(position[1]))-1
#Convert the value Y-axis to compatible with index number with -1


#Convert the value X-axis to numerical
if x == 'a':
    x = 0
elif x == 'b':
    x = 1
else:
    x = 2


map[y][x] = 'X'



# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")