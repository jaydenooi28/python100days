print("The Love Calculator is calculating your score...")
name1 = input('What is your name = ') # What is your name?
name2 = input('What is your partner name = ') # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

# name1 = "Angela Yu"
# name2 = "Jack Bauer"

lower_name1 = name1.lower()
lower_name2 = name2.lower()

combine_name = lower_name1 + lower_name2

#Calculate the number of times "TRUE" occours 
true = (combine_name.count('t')+combine_name.count('r')+combine_name.count('u')+combine_name.count('e'))

#Calculate the number of times "LOVE" occours 
love = (combine_name.count('l')+combine_name.count('o')+combine_name.count('v')+combine_name.count('e'))

#combine the numbers
love_score = str(true) + str(love)
int_love_score = int(love_score)


if int_love_score<10 or int_love_score>90:
    print (f'Your score is {love_score}, you go together like coke and mentos.' )
elif 40<int_love_score<50:
    print (f"Your score is {love_score}, you are alright together.")
else: 
    print (f"Your score is {love_score}.")