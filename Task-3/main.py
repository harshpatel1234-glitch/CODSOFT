# Password Generator

import random
import string

pass_len = int(input("Enter the desired password length: "))

if pass_len < 6:
    print("Password length should be at least 6 characters.")
else:
    all_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for _ in range(pass_len))

    print("Generated password:", password)