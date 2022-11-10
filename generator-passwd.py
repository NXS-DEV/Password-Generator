
import string
import random

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

generate = letters + numbers + symbols

length = 20

password = "".join(random.sample(generate, length))

print(password)



# Next update : Add GUI(Graphic User Interface)