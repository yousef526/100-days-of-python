""" # *args used to take many **postional argumetns** as wanted and they are in form of tuple datatype  

"""
def add(*args):
    total = 0
    print(type(args))# the type of *Args is a tuple
    print(args)
    for n in args:
        total+=n

    print(total)

add(5,53,4,5,89,6,2,8,2,83,87,89,2,8,1,8,4)


"""
**kwargs many keyword arguments 
it means i can give many word arguments 
 """

def cal(**kwargs):
    print(type(kwargs))# it has dictonary type
    print(kwargs)
    print(kwargs['x']+kwargs['y']+kwargs['m'])

cal(x=2,y=2,m=33)


