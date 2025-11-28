import random
from collections import Counter

def g():
    # Generate a random 4-digit number with unique digits
    digits = list("0123456789")
    key = "".join(random.sample(digits, 4))
    return key

def check(guess):
    # Check guess validity: 4 digits, no repeats
    if len(guess) != 4:
        return "Guess must be 4 digits."
    if not guess.isdigit():
        return "Guess must contain digits only."
    if len(set(guess)) != 4:
        return "Digits must not repeat."
    return None

def count_key(key, guess):
    # Count correct positions
    positions = sum(1 for k, g in zip(key, guess) if k == g)

    # Count digit matches
    key_freq = Counter(key)
    guess_freq = Counter(guess)
    total_matches = sum(min(key_freq[d], guess_freq[d]) for d in key_freq)

    exist = total_matches - positions
    return positions, exist

def display_history(history):
    print("\n--- Guess History (Last 6) ---")
    if not history:
        print("No guesses yet.")
    else:
        for entry in history[-6:]:
            print(f"  {entry['guess']} -> position:{entry['pos']} exist:{entry['exist']}")
    print("-----------------------------\n")

def start():
    print("Numerical Mastermind (4 digits, no repeats)\n")

    # Random secret key
    key = g()

    history = []

    # Main loop
    for attempt in range(1, 13):
        display_history(history)

        guess = input(f"Guess {attempt}: ").strip()
        err = check(guess)
        if err:
            print(err)
            continue

        if guess == key:
            print(f"\nCorrect! The key was {key}")
            return

        pos, exist = count_key(key, guess)

        history.append({
            "guess": guess,
            "pos": pos,
            "exist": exist
        })

    print("\nGame Over!")
    print("The key was:", key)

start()


