print("=" * 45)
print("🤖 Welcome to the Basic Chatbot!")
print("Type 'bye' anytime to exit.")
print("=" * 45)

while True:
    user = input("\nYou: ").lower()

    if user == "hello":
        print("Bot: Hello! Nice to meet you.")
    elif user == "hi":
        print("Bot: Hi! How are you?")
    elif user == "how are you":
        print("Bot: I'm doing great. Thanks for asking!")
    elif user == "what is your name":
        print("Bot: I'm CodeAlpha ChatBot.")
    elif user == "who created you":
        print("Bot: I was created using Python.")
    elif user == "bye":
        print("Bot: Goodbye! Have a great day!")
        break
    else:
        print("Bot: Sorry, I don't understand that.")