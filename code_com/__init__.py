# Import submodules for easier access
from . import basic_calculator
from . import chatbot
from . import math_utils
from . import minigames

# Import commonly used classes for direct access
from .basic_calculator import BasicCalculator
from .chatbot import Chatbot
from .math_utils import MathUtils

__version__ = "0.1.0"
__author__ = "Be1l"

__all__ = [
    'basic_calculator',
    'chatbot',
    'math_utils',
    'minigames',
    'BasicCalculator',
    'Chatbot',
    'MathUtils',
]
