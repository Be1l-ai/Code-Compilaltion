# Code Compilation

Collection of Python projects I built while learning programming fundamentals. Started with simple calculators and gradually added more complex features like web interfaces and mini-games.

## What's Inside

### Calculators (progression of complexity)
- **basic_calculator** - My first project. Does +, -, *, / with error handling
- **calculator** - Added expression evaluation, power, and square functions
- **advance_calculator** - Same logic but with Flask web interface and clickable buttons

### Mini Games
- **Jack en Poy** - Rock paper scissors
- **Number Guessing** - Classic guessing game with attempts counter
- **Math Quiz** - Timed math problems with scoring

### Utilities
- **math_utils** - Reusable math functions (factorial, GCD, LCM, prime checker)
- **chatbot** - Basic keyword-matching chatbot (no AI, just pattern matching)

## Project Structure

```
code_com/                    # main package
├── basic_calculator/
├── calculator/
├── advance_calculator/      # Flask web app
├── chatbot/
├── math_utils/
├── minigames/
└── documentations/          # detailed docs for each module
```

## Quick Start

**Try the web calculator:**
```bash
pip install -r requirements.txt
python3 code_com/advance_calculator/advance_calculator.py
# open http://localhost:5000/advance_calculator
```

**Play a game:**
```bash
python3 code_com/minigames/jack_en_poy.py
```

**Use math utils as a library:**
```python
from code_com.math_utils import MathUtils

MathUtils.factorial(5)  # returns 120
MathUtils.is_prime(7)   # returns True
```

## What I Learned

This project helped me understand:
- **OOP concepts** - classes, methods, inheritance
- **Package structure** - organizing Python projects with `__init__.py`
- **Web development** - Flask basics, routing, templating
- **Error handling** - try/except, input validation
- **Documentation** - writing READMEs and module docs

## Known Issues & Improvements

Things I know need work (learning in progress):
- Calculator uses `eval()` for expressions - works but not production-safe. Kept it simple for learning purposes
- Chatbot is very basic (keyword matching only, no actual AI)
- No unit tests yet - planning to add pytest coverage
- Some error handling could be more robust
- Mini-games could track high scores (maybe add SQLite?)

## Tech Stack

- Python 3.x
- Flask (for web calculator)
- Standard library otherwise

## Notes

This repo is basically my "learning playground." Code isn't perfect but it all works. Each project built on what I learned from the previous one. The three calculator versions show progression from CLI → advanced features → web interface.

Not meant to be production code - just practice projects that helped me learn Python fundamentals.
