import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!','#','$','%','&','(',')','*','+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# for num in range(1,10):
#     numbers.append(num)
# print(numbers)

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#easy level - order no random


#create a list for letters
num_of_letter = 0
letter_list  = [] 
while num_of_letter < nr_letters:
    letter_length = random.randint(0,len(letters)-1)
    random_letter = letters[letter_length]
    letter_list.append(random_letter)
    num_of_letter +=1
# print(letter_list)
#create a list for symbols
num_of_symbols = 0
symbol_list = []
while num_of_symbols < nr_symbols:
    symbol_length = random.randint(0,len(symbols)-1)
    random_symbols = symbols[symbol_length]
    symbol_list.append(random_symbols)
    num_of_symbols += 1
# print(symbol_list)
#create a list of numbers
num_of_numbers = 0
number_list = []
while num_of_numbers < nr_numbers:
    number_length = random.randint(0,len(numbers)-1)
    random_number = numbers[number_length]
    number_list.append(random_number)
    num_of_numbers +=1

# print(number_list)

#combine 3 list
letter_list.extend(symbol_list)
letter_list.extend(number_list)

password2 = letter_list.copy()
password1 = letter_list
# print (letter_list)

#ordered

password1 = ''.join(password1)
print("Ordered")
print(f"Your new password is :{password1}")

#randomized placement
random.shuffle(password2)
new_password2 = ''.join(password2)
print(f"Your new randomized password is :{new_password2}")

