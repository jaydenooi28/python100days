# Write your code below this line 👇
import math
def prime_checker (number):
    is_prime = True
    if number <= 1:
        is_prime = False
    else:
        if number%2 == 0:
            if number == 2:
                is_prime = True
            else:
                is_prime = False
        else:
            for i in range (3, int(math.sqrt(number))+1,2):
                if number%i == 0:
                    is_prime = False
    if is_prime == True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

                
        


# Write your code above this line 👆
    
#Do NOT change any of the code below👇
while  True:
    n = int(input("haha = ")) # Check this number
    prime_checker(number=n)