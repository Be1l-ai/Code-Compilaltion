# Code-Compilaltion

Python code repository with calculators, utilities, and mini-games.

## Structure

- **basic_calculator** — Basic arithmetic operations
- **calculator** — Extended calculator with square, power, evaluate
- **advance_calculator** — Flask web calculator
- **chatbot** — Simple keyword-based chatbot
- **math_utils** — Math utilities (factorial, prime check, gcd, lcm)
- **minigames** — Small CLI games

```
├── code_com/                      # main package with all the code
│   ├── __init__.py               # package initialization
│   ├── basic_calculator/         # simple calculator
│   │   ├── __init__.py
│   │   └── basic_calculator.py  # does +, -, *, /
│   ├── calculator/               # better calculator
│   │   ├── __init__.py
│   │   └── calculator.py        # expressions, power, square, etc
│   ├── advance_calculator/       # web calculator
│   │   ├── __init__.py
│   │   ├── advance_calculator.py # Flask app
│   │   └── templates/
│   │       └── advance_calculator.html
│   ├── chatbot/                  # simple chatbot
│   │   ├── __init__.py
│   │   └── chatbot.py           # keyword-based responses
│   ├── math_utils/               # math functions
│   │   ├── __init__.py
│   │   └── math_utils.py        # factorial, gcd, prime check, etc
│   ├── minigames/                # collection of games
│   │   ├── __init__.py
│   │   ├── jack_en_poy.py       # rock paper scissors
│   │   ├── number_guessing_game.py
│   │   └── quiz_game.py         # math quiz
│   │
│   └── documentations/           # docs for each module
│       ├── basic_calculator_docu.md
│       ├── calculator_docu.md
│       ├── advance_calculator_docu.md
│       ├── chatbot_docu.md
│       ├── math_utils_docu.md
│       └── minigames_docu.md
│
├── tests/                        # test files
├── requirements.txt              # dependencies
└── README.md                     # this file!
```

## The Projects

### 1. Basic Calculator

my first project! does basic math operations.

**Features:**
- addition, subtraction, multiplication, division
- division by zero protection
- simple terminal interface

**Run it:**
```bash
python3 code_com/basic_calculator/basic_calculator.py
```

### 2. Calculator (Advanced)

upgraded version with more features!

**Features:**
- everything from basic calculator
- square and power functions
- expression evaluation (like "2+3*4")
- uses eval() (i know its not the safest but it works lol)

**Run it:**
```bash
python3 code_com/calculator/calculator.py
```

---

### 3. Advanced Calculator (Web)

same calculator but with a web interface!

**Features:**
- nice looking web UI
- clickable buttons
- runs in browser
- powered by Flask

**Run it:**
```bash
python3 code_com/advance_calculator/advance_calculator.py
```

then open http://localhost:5000/advance_calculator in your browser

---

### 4. Chatbot

simple conversational bot with predefined responses.

**Features:**
- responds to greetings and simple questions
- keyword matching
- keeps chatting until you say exit

**Run it:**
```bash
python3 code_com/chatbot/chatbot.py
```

---

### 5. Math Utilities

collection of useful math functions.

**Features:**
- factorial calculation
- prime number checker
- GCD (greatest common divisor)
- LCM (least common multiple)

**Use it:**
```python
from code_com.math_utils import MathUtils

MathUtils.factorial(5)  # 120
MathUtils.is_prime(7)   # True
MathUtils.gcd(48, 18)   # 6
```

---

### 6. Mini Games

three simple games to play!

**Games:**
1. **Jack en Poy** - rock paper scissors
2. **Number Guessing** - guess the secret number
3. **Math Quiz** - answer math problems, get points

**Run any game:**
```bash
python3 code_com/minigames/jack_en_poy.py
python3 code_com/minigames/number_guessing_game.py
python3 code_com/minigames/quiz_game.py
```

## Documentation

- [Basic Calculator](code_com/documentations/basic_calculator_docu.md)
- [Calculator (Advanced)](code_com/documentations/calculator_docu.md)
- [Advanced Calculator (Web)](code_com/documentations/advance_calculator_docu.md)
- [Chatbot](code_com/documentations/chatbot_docu.md)
- [Math Utilities](code_com/documentations/math_utils_docu.md)
- [Mini Games](code_com/documentations/minigames_docu.md)

## What I Learned

making these projects taught me a lot:
- **OOP** - classes, inheritance, methods
- **user input/output** - handling user interaction
- **error handling** - try/except, validation
- **Flask** - web development basics
- **package structure** - organizing python projects
- **documentation** - writing docs (like this!)

## Tech Stack

- **Python 3** - main language
- **Flask** - web framework for advance calculator
- just standard library stuff otherwise

## Known Issues / TODO

things i need to fix or add:
- [ ] calculator uses eval() (security concern but works for now)
- [ ] chatbot is super basic (no AI, just keywords)
- [ ] no unit tests yet (should add those)
- [ ] could use better error handling in some places
- [ ] minigames could have more features
- [ ] maybe add a database for saving high scores?

**note:** this whole project is a work in progress. im still learning so the code might not be perfect. but it works and i learned a ton making it!
