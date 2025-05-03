import random
import string

def random_string_geerator(size=5,chars=string.ascii_lowercase+string.digits):
    return  ''.join(random.choice(chars) for x in range(size))

