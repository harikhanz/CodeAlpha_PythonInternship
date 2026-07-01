import random

# List of predefined words
words = ["python", "computer", "programming", "developer", "hangman"]

# Randomly choose a word
word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

print("=" * 40)
print("🎮 Welcome to Hangman Game!")
print("Guess the word one letter at a time.")
print(f"You have {max_guesses} incorrect guesses.")
print("=" * 40)

while incorrect_guesses < max_guesses:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only one alphabet letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct Guess!")
    else:
        incorrect_guesses += 1
        remaining = max_guesses - incorrect_guesses
        print("❌ Wrong Guess!")
        print(f"Remaining Chances: {remaining}")

else:
    print("\n💀 Game Over!")
    print("The correct word was:", word)