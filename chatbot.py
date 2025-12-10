import datetime

print("🤖 Simple Python Chatbot")
print("Type 'bye' to exit.\n")

def get_time():
    return datetime.datetime.now().strftime("%I:%M %p")

def get_date():
    return datetime.datetime.now().strftime("%d-%m-%Y")

responses = {
    "hi": "Hello! How can I help you?",
    "hello": "Hi there! What would you like to ask?",
    "how are you": "I'm doing great, thank you!",
    "your name": "I am a simple Python Chatbot.",
    "what is your name": "I am a simple Python Chatbot.",
    "time": f"The current time is {get_time()}",
    "date": f"Today's date is {get_date()}",
    "weather": "I'm not connected to the internet, but the weather is always perfect for learning!",
    "joke": "Why did the computer get cold? Because it forgot to close its Windows! 😄",
    "thanks": "You're welcome!",
}

while True:
    user = input("You: ").lower()

    if user == "bye":
        print("Bot: Goodbye! Have a nice day!")
        break

    elif user in responses:
        print("Bot:", responses[user])

    else:
        print("Bot: I don't understand that, but I'm learning!")
