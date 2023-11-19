from tkinter import messagebox
from passwordGenerator import PasswordGenerate
from tkinter import *
import json
# ---------------------------- Search emails ------------------------------- #
def search_website():
    try:
        with open('information.json','r') as f:
            data = json.load(f) # read old data
    except FileNotFoundError:
        messagebox.showinfo(title="Oops",message="No data file found")
    else:
        if website_entry.get().lower() in data:
            msg = f"""email: {data[website_entry.get().lower()]['email']}
            \nPassword: {data[website_entry.get().lower()]['password']}"""
            messagebox.showinfo(title="Sucess",message=msg)
        elif website_entry.get() == '':
            messagebox.showinfo(title="Oops",message="Enter valid data")
        else:
            messagebox.showinfo(title="Oops",message="Your website is not in records")
    

# ---------------------------- PASSWORD GENERATOR ------------------------------- #



def pop_up(msg,title,is_ok):
    if not is_ok:
        messagebox.showinfo(title=title,message=msg)
    else:
        msg = f"""These are the details entered:
        \nEmail: {UserName_entry.get()}
        \nPassword: {password_entry.get()}
        \n Is it ok to save?"""
        save = messagebox.askokcancel(title=title,message=msg)
        return save


def generate_Password():
    password_entry.delete(0,END)
    password_generator = PasswordGenerate() 
    password_entry.insert(END,string=password_generator.generatePass())
# ---------------------------- SAVE PASSWORD ------------------------------- #
def savePassword():
    # check that there is no empty field
    if website_entry.get() == '' or UserName_entry.get() == "" or password_entry.get() == "":
        pop_up(msg="Please don`t leave any fields empty!",title="Oops",is_ok=False)

    # save after check
    else:
        new_data = {
            website_entry.get().lower():{
                'email':UserName_entry.get(),
                'password':password_entry.get(),
            }
        }
        
        try:
            with open('information.json','r') as f:
                data = json.load(f) # read old data
                data.update(new_data)# update the old data
        except FileNotFoundError:
            with open('information.json','w') as f:
                json.dump(new_data,f,indent=4)# save the new data after update
        else:
            with open('information.json','w') as f:
                json.dump(data,f,indent=4)# save the new data after update
        website_entry.delete(0,END)
        password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

"""
using here columnspan zero could help
"""


window = Tk()
window.config(padx=50,pady=50)
window.title("Password Generator")

img_lock = PhotoImage(file='logo.png')
logo = Canvas(width=200,height=200)
logo.create_image(100,100,image=img_lock)
logo.grid(column=1,row=0)

#entries
website_entry = Entry(width=33,)
website_entry.focus()
website_entry.grid(column=1,row=2)

UserName_entry = Entry(width=51)
UserName_entry.insert(END,string="CaptinBlack123@Gmail.com")
UserName_entry.grid(column=1,row=3,columnspan=2)

password_entry = Entry(width=33)
password_entry.grid(column=1,row=4,)

#Labels
website_label = Label(text="Website",)
website_label.grid(column=0,row=2)

UserName_label = Label(text="Email/Username:")
UserName_label.grid(column=0,row=3)

password_label = Label(height=1,text='password')
password_label.grid(column=0,row=4)


# Buttons
search_btn = Button(width=14,text='Search',bg='white',command=search_website)
search_btn.grid(column=2,row=2)

generate_btn = Button(width=14,text='Generate password',background='white',command=generate_Password)
generate_btn.grid(column=2,row=4,)

save_pass = Button(text='Add',width=44,bg='white',command=savePassword,highlightthickness=0)
save_pass.grid(column=1,row=5,columnspan=2)

window.mainloop()




""" with open('information.txt','a') as f:
                f.write(f"{website_entry.get()} | {UserName_entry.get()} | {password_entry.get()}\n") """