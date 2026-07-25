import itertools
import string
import time

def dictionary_attack(password, wordlist):
    attempts = 0
    for word in wordlist:
        attempts += 1
        if word.strip() == password:
            return True, attempts
    return False, attempts

def brute_force_attack(password, max_length=4):
    chars = string.ascii_lowercase + string.digits
    attempts = 0
    start = time.time()

    for length in range(1, max_length + 1):
        for attempt in itertools.product(chars, repeat=length):
            attempts += 1
            guess = ''.join(attempt)
            if guess == password:
                end = time.time()
                return True, attempts, f"Cracked in {end-start:.2f} seconds"

    return False, attempts, "Password not cracked within limit"

