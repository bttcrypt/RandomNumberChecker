import random

def generate_random_number():
    return random.randint(1, 100)

def check_even_odd(number):
    if number % 2 == 0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")

random_number = generate_random_number()
check_even_odd(random_number)
