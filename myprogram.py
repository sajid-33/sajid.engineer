def greet(name):
    return f"Hello, {name}!"
from main import greet

def test_greet():
    assert greet("World") == "Hello, World!"
