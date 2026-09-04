def decorator(func):
    def wrapper(*args,**kwargs):
        print("before")
        result= func(*args,**kwargs)
        print("after")
        print(result)
    return wrapper

@decorator
def add(a,b):
    return a+b

add(10,50)
