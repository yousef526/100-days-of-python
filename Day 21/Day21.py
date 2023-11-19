# To make inheritance from parent class to sub class we put other class as argument 

# example

class Animal():
    def __init__(self):
        self.eyes = 4

    def play(self):
        print("Parent class")

class Fish(Animal):
    def __init__(self):
        super().__init__()####### very important as it calls parent class constrcutor

    def normal(self):
        print("Normal")
    
    def play(self):
        super().play()# to get what is made by the super class
        print("sub class")

fish = Fish()
#print(fish.eyes)
#fish.play()

## some notes on slicing

lis = [1,2,3,4,5,6,7,8,9,10]

print(lis[4:]) # take elements starting from fourth element
print(lis[2:5])# take elements starting from second element and until fourth element , fifth elment excluded
print(lis[2:5:2])# does the prevoius thing but taking +=2 not +=1 (increase by 2 numbers not 1)
print(lis[::2]) # normal loop but increase by 2
print(lis[::-1]) # reverse array as it starts from -1 element which is last element in python
                # as python have indcies by negative

