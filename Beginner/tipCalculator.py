print ('Welcome to the top calculator')
total_bill = input('What was the total bill? $')
tips_percent = input('What percentage tip would you like to give? 10,12,or 15?')
actual_tips = (float(tips_percent)/100)+1
how= float(input ('How many people to split the bill? '))
tips_given = (float(total_bill)/how)*actual_tips
pay = round(tips_given,2)
print (f"Each person should pay: ${pay}")
