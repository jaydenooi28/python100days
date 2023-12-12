alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from caesarart import logo
game_on = True
while game_on:
    print (logo)
    direction = (input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")).lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(what,message,number):
        message_list = [char for char in message]
        for i in message_list:
            if i in alphabet:
                # get the index number in the message and alphabet
                message_index_num = int (message_list.index(i))
                index_in_alpha = int (alphabet.index(i))
                # calculate the shift number
                if what == "encode":
                    code_index_num = index_in_alpha + number
                    while code_index_num > len(alphabet)-1:
                        code_index_num -= 26
                elif what == "decode":
                    code_index_num = index_in_alpha - number
                    while code_index_num < 0:
                        code_index_num += 26

                message_list[message_index_num] = alphabet[code_index_num]
        final_message = "".join(message_list)
        print(f"Message = {final_message}")
    caesar(what = direction, message = text, number=shift)
    ask_user = True
    while ask_user:
        ans = (input("Do you want to continue?\n[y/n] ")).lower()
        if ans == "y":
            ask_user = False
            game_on = True
            break
        elif ans == "n":
            ask_user = False
            game_on = False
  
        else:
            print("bro please answer correctly")

        



    


