""" # what is default arguments
what is *Args
What is **Kwargs
What is GUI """


from tkinter import *

window = Tk()
#window.maxsize(height=300,width=500)# to configure the size of screen when it is maximized (max size)
window.minsize(height=300,width=500)# to make minimus size when screen openn
window.title("Hello")# used to change the title of window program



# make a label to show on screen
myLabel = Label(text="Hello world",font=('Aerial',25,"bold"))

# to make anythin show on tkinter screen must specify the location 
#myLabel.pack(side='left')
#myLabel.place(x=500,y=300)
myLabel.grid(column=0,row=0)

def event():
    myLabel['text'] = "Got clicked"
    myLabel['text'] = input_.get()


btn = Button(text='Press me',command=event)
btn.config(fg='green',bg='red')
#btn.pack(side='left')
#btn.place(x=500,y=300)
btn.grid(column=1,row=1)

new_btn = Button(text='Press me')
new_btn.config(fg='green',bg='red')
#new_btn.pack(side='left')
#new_btn.place(x=500,y=300)
new_btn.grid(column=3,row=0)

input_ = Entry(width=10)
input_.insert(END,"HELlo")
#input_.pack(side='left')
#input_.place(x=500,y=300)
input_.grid(column=5,row=5)


# it is ued to keep window on screen
window.mainloop()


################################################################
# 3 important things for tkinter Pack()  Place()  Grid()