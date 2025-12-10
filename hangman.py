import random

words = ["apple", "python", "flower", "happy", "cloud"]
word = random.choice(words)

guessed = ["_"] * len(word)
attempts = 6

print("🎮 Hangman Game!")
print("Guess the word:")

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Attempts left:", attempts)

    letter = input("Enter a letter: ").lower()

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
        print("Correct letter!")
    else:
        attempts -= 1
        print("Wrong letter!")

if "_" not in guessed:
    print("\n🎉 You win! The word is:", word)
else:
    print("\n❌ You lost! The word was:",word)
