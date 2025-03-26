from .main import QuickMethods
import math

class Number():
    """
    # BETA:
    ## Subject to change without warning.
    
    ---
    
    A simple class to deal with both float and int numbers.
    """
    def __init__(self, x: int | float | str):
        if type(x) != int and type(x) != float and type(x) != str:
            raise ValueError(f"{type(x).__name__} '{x}' is invalid.")
        if not QuickMethods().string_is_number(str(x)):
            raise ValueError(f"'{x}' is not a valid number.")
        
        self.x_number: float | int = complex(x).real
        if self.x_number.is_integer():
            self.x_number = int(self.x_number)
    
    def __str__(self):
        return str(self.x_number)
    
    def __repr__(self):
        return str(f"Number({type(self.x_number).__name__}({self.x_number}))")
    
    def __eq__(self, other_value):
        if isinstance(other_value, Number):
            return self.x_number == other_value.x_number
        else:
            return self.x_number == other_value
    
    def __ne__(self, other_value):
        if isinstance(other_value, Number):
            return self.x_number != other_value.x_number
        else:
            return self.x_number != other_value
    
    def __lt__(self, other_value):
        if isinstance(other_value, Number):
            return self.x_number < other_value.x_number
        else:
            return self.x_number < other_value
    
    def __le__(self, other_value):
        if isinstance(other_value, Number):
            return self.x_number <= other_value.x_number
        else:
            return self.x_number <= other_value

    def __ge__(self, other_value):
        if isinstance(other_value, Number):
            return self.x_number >= other_value.x_number
        else:
            return self.x_number >= other_value

    def __add__(self, other_value: float | int):
        if isinstance(other_value, Number):
            return self.x_number + other_value.x_number
        return self.x_number + other_value

    def __radd__(self, other_value: float | int):
        if isinstance(other_value, Number):
            return self.x_number + other_value.x_number
        return self.x_number + other_value

    def __sub__(self, other_value: float | int):
        if isinstance(other_value, Number):
            return self.x_number - other_value.x_number
        return self.x_number - other_value
        
    def __rsub__(self, other_value: float | int):
        if isinstance(other_value, Number):
            return self.x_number - other_value.x_number
        return self.x_number - other_value

    def __mul__(self, other_value: float | int):
        if isinstance(other_value, Number):
            return self.x_number * other_value.x_number
        return self.x_number * other_value
    
    def __rmul__(self, other_value: float | int):
        if isinstance(other_value, Number):
            return self.x_number * other_value.x_number
        return self.x_number * other_value

    def __truediv__(self, other_value: float | int):
        if isinstance(other_value, Number):
            return self.x_number / other_value.x_number
        return self.x_number / other_value
    
    def __rtruediv__(self, other_value: float | int):
        if isinstance(other_value, Number):
            return other_value.x_number / self.x_number
        return other_value / self.x_number
    
    def __pow__(self, other_value: float | int):
        if isinstance(other_value, Number):
            return self.x_number ** other_value.x_number
        return self.x_number ** other_value

    def __rpow__(self, other_value: float | int):
        if isinstance(other_value, Number):
            return other_value.x_number ** self.x_number
        return other_value ** self.x_number
    
    def __round__(self, ndigits: None = None):
        rounded_value = int(self.x_number)
        if ndigits:
            rounded_value = round(self.x_number, ndigits)
        return rounded_value
    
    def __neg__(self):
        return -self.x_number
    
    def __invert__(self):
        return ~self.x_number
    
    def __or__(self, other_value):
        return self.x_number | other_value
    
    def __ror__(self, other_value):
        return other_value | self.x_number
    
    def __and__(self, other_value):
        return self.x_number & other_value

    def __rand__(self, other_value):
        return other_value & self.x_number
    
    def __ceil__(self):
        return math.ceil(self.x_number)
    
    def __floor__(self):
        return math.floor(self.x_number)
    
    def is_int(self) -> bool:
        return type(self.x_number) == int

    def is_float(self) -> bool:
        return type(self.x_number) == float

    def is_even(self) -> bool:
        """
        Even numbers are numbers that can be divided by 2 without leaving a remainder.
        """
        number_to_check: int = self.x_number
        if type(number_to_check) is not int:
                raise ValueError(f"{type(self.x_number).__name__} '{self.x_number}' is invalid: only integers can be classified as even or odd.")
        return (self.x_number / 2).is_integer()