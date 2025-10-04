class Chatbot:
    def __init__(self):
        self.responses = {
            "hello": "Hi there! How can I help you?",
            "how are you": "I'm just a bot, but I'm doing fine! How about you?",
            "what's your name": "I'm a simple chatbot created in Python!",
            "bye": "Goodbye! Have a great day!"
        }

    def chat(self):
        while True:
            user_input = input("You: ").lower()
            if user_input in self.responses:
                print("Chatbot:", self.responses[user_input])
            elif user_input == "exit":
                print("Chatbot: Goodbye!")
                break
            else:
                print("Chatbot: Sorry, I don't understand that.")

if __name__ == "__main__":
    print("Simple Chatbot. Type 'exit' to stop.")
    bot = Chatbot()
    bot.chat()
