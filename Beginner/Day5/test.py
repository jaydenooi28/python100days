import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!','#','$','%','&','(',')','*','+']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

inpl = 4
inps = 4
inpn = 4
num_of_letter = 0
letter_list  = [] 
while num_of_letter < inpl:
    letter_length = random.randint(0,len(letters)-1)
    random_letter = letters[letter_length]
    letter_list.append(random_letter)
    num_of_letter +=1
print (letter_list)