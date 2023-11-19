"""from turtle import Turtle , Screen

timmy  = Turtle()
timmy.shape("turtle")
timmy.color('AliceBlue')
timmy.fillcolor('red')
timmy.shapesize(10,10,10)
io = 5
while io:
    #timmy.forward(100)
    timmy.fd(200)
    timmy.fd(-200)
    timmy.fd(-200)
    timmy.fd(200)
    io -= 1
    
my_screen = Screen()

my_screen.exitonclick()"""

from prettytable import PrettyTable
# table = PrettyTable()
# table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
# table.add_row(["Adelaide", 1295, 1158259, 600.5])
# table.add_row(["Brisbane", 5905, 1857594, 1146.4])
# table.add_row(["Darwin", 112, 120900, 1714.7])
# table.add_row(["Hobart", 1357, 205556, 619.5])
# table.add_row(["Sydney", 2058, 4336374, 1214.8])
# table.add_row(["Melbourne", 1566, 3806092, 646.9])
# table.add_row(["Perth", 5386, 1554769, 869.4])
# print(table)
# table.add_column("sex",column=['Male',"Female",'Male',"Female",'Male',"Female",'Male'])

table2 = PrettyTable()
table2.add_column("Pokemon Name",column=["Pikachu","Squirtle","Charmander"])
table2.add_column("Type",column=["Electric*","Water","Fire"])
print(table2)
table2.align = 'l'
print(table2)