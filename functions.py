def load_words(path):
    """Return a list of words read from `path` (one per line)."""

    with open(path) as f:
        return [line.strip() for line in f if line.strip()]


def build_display(secret, correct):
    """Return the word with unguessed letters replaced by '_'."""
    return " ".join(char if char in correct else "_" for char in secret)


def check_word(correct, incorrect, secret, wrong):
    guess = input("Guess a letter: ").lower()
    
    if guess.isalpha() == False or len(guess) != 1:
        print("Not a valid guess; please enter a single letter")
    elif guess in correct or guess in incorrect:
        print("You already guessed that")
    elif guess in secret:
        correct.append(guess)
    else:
        incorrect.append(guess)
        wrong += 1
    return wrong

def clear_screen():
    print("\n" * 50)

def introduction(name):
    print(f'''
================================
Welcome to ArachnoPhonics, {name}!
Guess the word before the Spider finishes its web!
================================
          ''')
    

#Difficulty Levels Feature
def pick_difficulty():
    choice = input("Difficulty (easy/medium/hard): ").strip().lower()

    table = {'easy': 8, 'medium': 6, 'hard': 4}

    if choice == 'easy':
        max_wrong = table.get('easy')
    elif choice == 'medium':
        max_wrong = table.get('medium')
    elif choice == 'hard':
        max_wrong = table.get('hard')
    else:
        print("Not a valid choice, defaulting to medium")
        max_wrong = 6
        choice = 'medium'

    print(f"You chose {choice} — {max_wrong} wrong allowed.")
    return max_wrong