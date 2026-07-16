import random
import time

from functions import load_words, build_display, check_word, clear_screen, introduction, pick_difficulty
from spiderDraw import spider_0, spider_1, spider_2, spider_3, spider_4, spider_5, spider_6, spider_7, spider_8

SPIDER_STAGES = [spider_0, spider_1, spider_2, spider_3, spider_4, spider_5, spider_6, spider_7, spider_8]


def play_round(max_wrong):
    introduction(input("Your name: "))
    game = True
    words = load_words("words.txt")
    secret = random.choice(words).lower()
    correct = []
    incorrect = []
    wrong = 0

    while game:
        print("\nWelcome to ArachnoPhonics!")
        print(SPIDER_STAGES[wrong]())
        print("Word:", build_display(secret, correct))
        wrong = check_word(correct, incorrect, secret, wrong)
        time.sleep(2)

        if '_' not in build_display(secret, correct):
            game = False
        elif wrong >= max_wrong:
            game = False

        clear_screen()

        if not game:
            print(SPIDER_STAGES[wrong]())
            print("Word:", build_display(secret, correct))
    

def main():
    max_wrong = pick_difficulty()

    while True:
        play_round(max_wrong)

        again = input("Play Again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for Playing!")
            break

if __name__ == "__main__":
    main()
