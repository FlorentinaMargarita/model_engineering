import re

def has_all_caps(message):
    # Remove all non-alphabetic characters
    letters_only = re.sub("[^a-zA-Z]", " ", message)
    
    # Check if all the alphabetic characters are uppercase
    if letters_only.isupper():
        return 1
    else:
        return 0