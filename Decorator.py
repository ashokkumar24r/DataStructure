import functools

def decorators(func):
    #@functools.wraps(func)
    def new_decorators():
        print ("I am Inside the decorator")
        func()
        print("I am Outside the decorator")
    return new_decorators

@decorators
def funct():
    print ("Yes")

funct()
