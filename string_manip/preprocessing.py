import re

replace_with_space_1 = r'[\u0000-\u0040]'
replace_with_space_2 = r'[\u005b-\u0060]'

def remove_space_and_punctuation(text):
    new_text = ''
    for char in text:
        char = re.sub(replace_with_space_1, "", char)
        char = re.sub(replace_with_space_2, "", char)
        if char != "":
            char = char.lower()
        new_text += char
    return new_text
