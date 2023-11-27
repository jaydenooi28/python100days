# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

total_height = 0
number_of_student = 0
average_height = 0

#calculate total height
for t in student_heights:
  total_height += t
#calculate total number of student
  number_of_student +=1 
  
#calculate the average height
average_height += round((total_height/number_of_student))


print(f"total height = {total_height}")
print(f"number of students = {number_of_student}")
print(f"average height = {average_height}")