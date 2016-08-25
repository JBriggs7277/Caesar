from helpers import alphabet_position, rotate_character
from sys import argv, exit

def user_input_is_valid(cl_args):
    if  len(cl_args) > 1:
        if cl_args[1].isdigit():
            return True
    return False

def encrypt(text, rot):
    emptystr = ""
    for char in text:
        newchar = rotate_character(char, rot)
        emptystr = emptystr + newchar
    return emptystr

#if user_input_is_valid(argv) == False:
#    print("usage: python3 caesar.py n")
#    exit()
#text = input("Type a message:")
#print(text)
#rot = int(argv[1])
#print(encrypt(text, rot))
