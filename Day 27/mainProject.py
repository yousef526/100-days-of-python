from tkinter import *

window = Tk()

window.minsize(width=300,height=100)
window.title("Mile to Km Converter")
window.config(padx=10,pady=10)


entry_input = Entry()
entry_input.config(width=7)
entry_input.grid(column=1,row=0)


text1 = Label(text="Miles")
text1['padx'] = 10
text1.grid(column=2,row=0)

text2 = Label(text="is equal to")
text2['padx'] = 10
text2.grid(column=0,row=1)



text3 = Label(text="")
text3['width'] = 4
text3.grid(column=1,row=1)


text4 = Label(text="Km")
text4.grid(column=2,row=1)

def transform():
    miles = float(entry_input.get())
    km = miles * 1.6
    text3['text'] = round(km)

cal_btn = Button(text="Calculate",command=transform)
cal_btn.grid(column=1,row=2)


window.mainloop()