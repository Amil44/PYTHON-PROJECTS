import random

GREEN = '\033[92m'
YELLOW = '\033[93m'
GRAY = '\033[90m'
MAGENTA = "\033[35m"
RED = '\033[91m'
RESET = '\033[0m'

print(f"\t\t\t\t\t\t\t\t*****Welcome to the Game*****\n{MAGENTA}Get ready for an exciting adventure where every choice matters. Explore new worlds, overcome challenges, and test your skills.\nAre you ready to play, compete, and have fun? Your journey starts now!{RESET}")

r_words = [
    "rally","river","rapid","rough","reply","rebel","rated","reach","react",
    "round","royal","rinse","ravel","rusty","retro","recur","retry","roast",
    "raven","relax","right","ratio","rodeo","rhino","rigid","rains","ruler",
    "rowsy","racks","rants","rifts","ropes","ruins","rages","rides","rites",
    "rails","roomy","rabid","radii","ranch","rarer","rawer","razor","rebar",
    "rebus","redox","redux","relic","remit","renal","revel","rheum","reset",
    "roads","roots","rolls", "realm", "rolls", "roots", "rooms"
]

def main():
    target = random.choice(r_words)
    count_try = 5

    while count_try:
        print(f'\nYou have {count_try} guess.')
        guess_word = input("Guess the word: ").lower()

        if len(guess_word) != 5:
            print(f"{RED}Length of the word must be 5!{RESET}")
            continue
        if guess_word not in r_words:
            print(f"{RED}This word does not exist in list!{RESET}")
            continue

        count_try -= 1
        save_your_guess = ""
        target_letters = list(target)  
        output = [""] * 5 

        for i in range(5):
            if guess_word[i] == target_letters[i]:
                output[i] = f"{GREEN}{guess_word[i]}{RESET}"
                save_your_guess += guess_word[i]
                target_letters[i] = None  

        for i in range(5):
            if output[i] == "":
                if guess_word[i] in target_letters:
                    output[i] = f"{YELLOW}{guess_word[i]}{RESET}"

                    index = target_letters.index(guess_word[i])
                    target_letters[index] = None
                else:
                    output[i] = f"{GRAY}{guess_word[i]}{RESET}"

        print(" ".join(output))

        if save_your_guess == target:
            print(f"\n{GREEN}You Win! The word was '{target}'{RESET}")
            break
    else:
        print(f"\n{RED}You Lost! The word was '{target}'{RESET}")

main()
