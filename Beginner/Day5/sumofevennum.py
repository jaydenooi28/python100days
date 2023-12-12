target = int(input("Number = ")) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇

#create a list that contain even number
e_list=[]
for even in range (0,(target+1)):
    if even%2 == 0:
        e_list.append(even)
#add all the values
sum = sum(e_list)

print(sum)

