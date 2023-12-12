alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = (input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")).lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(message,number):
    message_list = [char for char in message]
    for i in message_list:
        if i in alphabet:
            message_index_num = int(message_list.index(i))
            # get the index number of alphabet in alphabet list
            index_in_alpha = int (alphabet.index(i))
            # calculate the shift number 
            encode_index_num = index_in_alpha + number
            if encode_index_num > (len(alphabet)) - 1 :
                while encode_index_num > (len(alphabet)) - 1 :
                    encode_index_num = encode_index_num - 26
            elif encode_index_num < 0:
                while encode_index_num < 0:
                    encode_index_num = encode_index_num + 26
            # convert the value to the new encoded char
            message_list[message_index_num] = alphabet[encode_index_num]
    # convert the list to string
    encoded_message = "".join(message_list)
    print(f"Encoded message = {encoded_message}")
 

def decrypt(message,number):
    message_list = [char for char in message]
    for i in message_list:
        if i in alphabet:
            message_index_num = int(message_list.index(i))
            # get the index number of alphabet in alphabet list
            index_in_alpha = int (alphabet.index(i))
            # calculate the shift number 
            decode_index_num = index_in_alpha - number
            # if the num is more than 25, keep minus 26 until less than 26
            while decode_index_num > (len(alphabet)) - 1:
                    decode_index_num = decode_index_num - 26
            # if the num is less than 0, keep adding 26 until more than 0
            while decode_index_num < 0:
                    decode_index_num = decode_index_num + 26
            # convert the value to the new encoded char
            message_list[message_index_num] = alphabet[decode_index_num]
    # convert the list to string
    decoded_message = "".join(message_list)
    print(f"Decoded message = {decoded_message}")



if direction == "encode":
    encrypt(message = text, number = shift)
elif direction == "decode":
    decrypt(message = text, number = shift)
else:
    print("Bro please enter correctly")