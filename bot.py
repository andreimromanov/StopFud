responses = [
    "Don’t panic, trust the fundamentals.",
    "Rumors fade, code stays.",
    "Stay focused, ignore the noise.",
]

import random

def reply():
    return random.choice(responses)

if __name__ == "__main__":
    print(reply())
