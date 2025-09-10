def chatbot():
    user_name=input("Chatbot: What is ur name? ")
    print("Chatbot: Hello! Type 'bye' to end the chat.")

    while True:
        user_input = input(f"{user_name}: ").lower()

        if user_input == "hello" or user_input=="hi":
            if user_name:
                print(f"Chatbot: Hi {user_name}!")
            else:
                print(f"Chatbot: Hi! {user_name}")

        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks! How about you?")

        elif user_input in ["i'm fine", "i am fine","i am good."]:
            print("Chatbot: Great to hear that!")

        elif user_input == "what is your name":
            print("Chatbot: My name is Alice.")

        elif user_input == "what is my name":
                print(f"Chatbot: Your name is {user_name}, right?")

        elif user_input.startswith("my name is"):
            name = user_input.replace("my name is", "").strip().capitalize()
            user_name = name
            print(f"Chatbot: Nice to meet you, {user_name}!")

        elif user_input == "how old are you":
            print("Chatbot: I'm ageless. I was created by a programmer.")

        elif user_input == "what is your favorite color":
            print("Chatbot: My favourite color is RED. ")

        elif user_input == "bye":
            if user_name:
                print(f"Chatbot: Goodbye, {user_name}! Have a great day!")
            else:
                print("Chatbot: Goodbye! Have a great day!")
            break

        else:
            print("Chatbot: Sorry, I don’t understand that.")


chatbot()
