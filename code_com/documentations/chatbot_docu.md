# Chatbot

Simple keyword-based CLI chatbot.

## Features

- Keyword matching for responses
- Basic conversation flow
- Predefined response dictionary
- Exit command support

## How to Use

### Run Directly

## Example Conversation

```
Chatbot is ready! (type 'exit' to quit)
----------------------------------------
You: hello
Chatbot: Hi there! How can I help you?
You: what's your name
Chatbot: I'm a simple chatbot created in Python!
You: how are you
Chatbot: I'm just a bot, but I'm doing fine! How about you?
You: thanks
Chatbot: You're welcome! Happy to help!
You: what's the weather
Chatbot: Sorry, I don't understand that. Try asking something else!
You: exit
Chatbot: Goodbye!
```

## How to Add New Responses

just edit the `__init__` method and add to the responses dictionary:

```python
self.responses = {
    "hello": "Hi there! How can I help you?",
    "your question": "your response here",
    # add more here
}
```

## Limitations

- **no AI** - just keyword matching
- **exact matches only** - "hello" works but "hello there" doesn't
- **no context** - forgets everything after each response
- **limited responses** - only knows what you program it to know
- **no learning** - won't get smarter over time

## What I Learned

- dictionaries in python
- while loops for continuous interaction
- user input handling
- string manipulation (.lower())

## Future Ideas

stuff i might add if i have time:
- [ ] fuzzy matching (so "helo" still works)
- [ ] multiple possible responses (randomize)
- [ ] conversation context/memory
- [ ] learn from conversations?
- [ ] integrate with real AI API
- [ ] GUI version
- [ ] more responses obviously
