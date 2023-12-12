list = []
for a in range (1, 101):
    list.append(a)

for f in list:
    if f%3 == 0 and f%5 == 0:
        print ("FizzBuzz")
    elif f%5 == 0:
        print ("Buzz")
    elif f%3 == 0:
        print ( "Fizz")
    else:
        print (f)