names_string = input ("Enter the list of names = ")
names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random

#calculate the total number of people from input
# -1 because index number count from 0
total_num_ppl = (len(names)) -1

roulette = random.randint(0,total_num_ppl)
paying_person = names[roulette]
print(f"{paying_person} is going to buy the meal today!")
