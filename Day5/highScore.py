# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
high_score = 0
for x in student_scores:
  if x > high_score:
    high_score = x
print(f"The highest score in the class is: {high_score}")
