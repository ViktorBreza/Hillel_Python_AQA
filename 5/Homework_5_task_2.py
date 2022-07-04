# Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float.
# Якщо перетворити не вдається функція має повернути 0 (флоатовий нуль).


def float_maker(arg):
    """Takes in data arg, returns the arg converted into float"""
    try:
        return float(arg)
    except ValueError:
        return 0




