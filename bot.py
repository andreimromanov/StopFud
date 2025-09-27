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

responses.append("research > rumors.")  # added 2025-09-27T19:10:01.735817
