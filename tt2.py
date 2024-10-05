


from typing import Callable


def hi_name(func: Callable, *args) -> Callable:
    def wrapper(*args):
        func(*args)
        print("Alexandr!")
    return wrapper





@hi_name
def hi(a):
    print("Hello")

@hi_name
def bye():
    print("Good bye")



hi(2)
