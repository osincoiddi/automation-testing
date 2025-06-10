
import random
import string
from random import choice
from string import ascii_lowercase

def generate_random_string(size=5,chars=string+ascii_lowercase+string.digits):
    return ''.join(choice(chars) for x in range(size))