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
    def __init__(self, x: int | float | complex):
        self.x_number: int | float | complex = x
    
    def __str__(self):
        return str(self.x_number)
    
    def __repr__(self):
        return str(f"Number({self.x_number})")
    
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
        number_is_int: bool = False
        if type(self.x_number) == int:
            number_is_int = True
        return number_is_int

    def is_float(self) -> bool:
        number_is_float: bool = False
        if type(self.x_number) == float:
            number_is_float = True
        return number_is_float

if __name__ == "__main__":
    qm = QuickMethods()
    print(repr(qm), end="\n\n")
    
    qm.say_hello()
    print(qm.string_is_number("7j"))
    
    first_value = Number(12)