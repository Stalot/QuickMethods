import getpass

class QuickMethods:
    def __init__(self):
        pass
    
    def __repr__(self):
        return "QuickMethods()"

    def say_hello(self) -> None:
        try:
            print(f"Hello, {getpass.getuser()}!")
        except:
            print("Hello! Hmm... I wasn't able to guess your name... Hello John Doe!")
    
    def string_is_number(self, string: str) -> bool:
        try:
            complex(string)
            return True
        except ValueError:
            return False


class Number():
    """    
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

    def __add__(self, other_value):
        if isinstance(other_value, Number):
            return self.x_number + other_value.x_number
        else:
            return self.x_number + other_value

    def __sub__(self, other_value):
        if isinstance(other_value, Number):
            return self.x_number - other_value.x_number
        else:
            return self.x_number - other_value

    def __mul__(self, other_value):
        if isinstance(other_value, Number):
            return self.x_number * other_value.x_number
        else:
            return self.x_number * other_value

    def __truediv__(self, other_value):
        if isinstance(other_value, Number):
            return self.x_number / other_value.x_number
        else:
            return self.x_number / other_value
    
    def __round__(self, ndigits: None = None):
        rounded_value = int(self.x_number)
        if ndigits:
            rounded_value = round(self.x_number, ndigits)
        return rounded_value
    
    def is_int(self) -> bool:
        return type(self.x_number) == int

    def is_float(self) -> bool:
        return type(self.x_number) == float

    def is_even(self) -> bool:
        """
        Even numbers are numbers that can be divided by 2 without leaving a remainder.
        """
        if type(self.x_number) is not int:
            raise ValueError(f"{type(self.x_number).__name__} '{self.x_number}' is invalid: only integers can be classified as even or odd.")
        return (self.x_number / 2).is_integer()

    def is_odd(self) -> bool:
        """
        Odd numbers are integers that cannot be divided by two without a remainder.
        """
        if type(self.x_number) is not int:
            raise ValueError(f"{type(self.x_number).__name__} '{self.x_number}' is invalid: only integers can be classified as even or odd.")
        return not (self.x_number / 2).is_integer()

if __name__ == "__main__":
    qm = QuickMethods()
    print(repr(qm), end="\n\n")
    
    qm.say_hello()
    print(qm.string_is_number("7j"))
    
    first_value = Number(12)
    second_value = Number(5)
    third_value = Number(24.4)
    
    for number in (first_value, second_value, third_value):
        print(f"\n{repr(number)}\nis even: {number.is_even()}\nis odd: {number.is_odd()}")