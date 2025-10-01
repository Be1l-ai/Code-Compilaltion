from .jack_en_poy import jack_en_poy
from .number_guessing_game import guess_number
from .quiz_game import math_prob

__version__ = "0.1.0"
__author__ = "Be1l"

# Define what is exported when using 'from minigames import *'
__all__ = [
    "jack_en_poy",
    "guess_number",
    "math_prob",
]