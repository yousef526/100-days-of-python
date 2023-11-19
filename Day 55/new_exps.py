""" class User():
    def __init__(self,name):
        self.name = name
        self.logged_on = False


def is_logged_on(func):
    def innner(**kwargs):

        if not kwargs['user'].logged_on:
            func(kwargs['user'])
    return innner

@is_logged_on
def new_User(user):
    print(f"Hello {user.name} to our new blog")

user22 = User("Abbas")

new_User(user=user22,ty="asdf",x=2,y=3,a=4) """

def logger(func):
    def wrap(*args):
        print(f"you called the function called {func.__name__}{args}")
        res = func(args[0],args[1],args[2])
        print(f"result is {res}")
    return wrap

@logger
def a_func(x,y,z):
    return x+y+z

a_func(1,2,3)