""" def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def cal(func,n1,n2):
    return func(n1,n2) """

#print(cal(add,2,3))

""" def outer():
    
    print("iam out")

    def inner():
        print("iam inner")

    inner()

outer() """


""" def outer():
    
    print("iam out")

    def inner():
        print("iam inner")

    return inner

x = outer()
x() """
###########################################################@#@#@#
import time

""" def decorater_func(function):
    def wrap_func():
        time.sleep(2)
        function()
    return wrap_func

def sah_b():
    print(":b")

def sah_c():
    print(":c")

@decorater_func
def sah_a():
    print(":a")

sah_a()
sah_b() """

current_time = time.time()
print(current_time)


def speed_calc_decorator(func):
    def cal_diff():
        func()
        print(time.time() - current_time)
    return cal_diff

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator 
def slow_function():
    for i in range(100000000):
        i * i

#fast_function()
slow_function()