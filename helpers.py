def alphabet_position(letter):
    if letter.isupper():
        pos = (ord(letter) - 65)
    else:
        pos = (ord(letter) - 97)
    return pos

def rotate_character(char, rot):
    if char.isupper():
        index = ((alphabet_position(char) + rot) % 26) + 65
        newchar = chr(index)
    elif char.islower():
        index = ((alphabet_position(char) + rot) % 26) + 97
        newchar = chr(index)
    else:
        newchar = char
    return newchar
