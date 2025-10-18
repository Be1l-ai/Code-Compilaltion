from . import basic_calculator
from . import calculator
from . import advance_calculator
from . import chatbot
from . import math_utils
from . import minigames

from .basic_calculator import BasicCalculator
from .calculator import Calculator
from .chatbot import Chatbot
from .math_utils import MathUtils

__version__ = "0.1.0"

__all__ = [
    'basic_calculator',
    'calculator',
    'advance_calculator',
    'chatbot',
    'math_utils',
    'minigames',
    'BasicCalculator',
    'Calculator',
    'Chatbot',
    'MathUtils',
]
