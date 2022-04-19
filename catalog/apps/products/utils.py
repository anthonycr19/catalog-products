import random
import string


def create_ramdom_string(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))
