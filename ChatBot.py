import random

def check_greeting(user_input):
    greetings = ["hello", "hi", "hey"]
    if user_input.lower() in greetings:
        return True
    else:
        return False

def main():
    responses = {
        # String on the left is the user input
        # String on the right is the ChatBot's possible input
        # *** The user input must be typed in exactly how it is shown
        # on the left side of the : ***
        "how are you?": ["I'm good, thanks!", "I'm doing great!", "Not too bad."],
        "what's your name?": ["My name is ChatBot.", "You can call me ChatBot.", "I'm ChatBot, nice to meet you!"],
        "bye": ["Goodbye!", "See you later!", "Take care!"] # Add a , here if you want to add new inputs
    }

    # Welcome message
    print("Welcome! Ask me anything or say bye to exit.")

    # These are the decision statements when
    # a user types in something
    while True:
        user_input = input("User: ")
        if user_input.lower() == "bye":
            print(random.choice(responses["bye"]))
            break
        elif check_greeting(user_input):
            print(random.choice(["Hello!", "Hi there!", "Hey!"]))
        else:
            found_response = False
            for key in responses:
                if user_input.lower() in key:
                    print(random.choice(responses[key]))
                    found_response = True
                    break
            if not found_response:
                print("I'm sorry, I don't understand.")

if __name__ == "__main__":
    main()