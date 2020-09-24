from python_startkit.model import a as a_model
from python_startkit.model2 import a as b_model

from .model import a as c_model

d_model = a_model + b_model + c_model
e_model = d_model + 5


def bla(e_e: int) -> int:
    return e_e + 5
