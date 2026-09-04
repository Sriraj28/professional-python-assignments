def decorator(func):

    def wrapper():
        print("before")
        func()
        print("after")

    return wrapper
@decorator
def greet():
    print("hello i'm in between both")

greet()