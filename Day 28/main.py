""" # a function that can loop inside the mainloop function called **window.after**
     # the arguments from left the 1000 =  1 sec , second arg it 
     # function to do operation  """
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = '✔'
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    timer_text['text'] ='Timer'
    check_mark_text['text'] = ""
    canvas.itemconfig(text_Timer,text="00:00")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_countDown():
    Work_sec = WORK_MIN * 60
    Short_break_sec = 60 * SHORT_BREAK_MIN
    Long_break_sec = LONG_BREAK_MIN * 60

    global reps
    reps+=1
    if reps % 2 != 0:
        timer_text.config(text='Working',fg=GREEN)
        count_down(Work_sec)

    elif reps == 8:
        reps = 0
        timer_text.config(text='Break',fg=RED)
        count_down(Long_break_sec)

    elif reps < 8 and reps % 2 == 0:
        timer_text.config(text='Break',fg=PINK)
        count_down(Short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    mins = count // 60
    seconds = count % 60
    if seconds < 10:
        seconds =f'0{seconds}'

    canvas.itemconfig(text_Timer,text =f"{mins}:{seconds}")

    if count > 0:
        global timer
        timer = window.after(1000,count_down,count - 1) #use it as global var to help in reset process
    else:
        start_countDown()
        if reps < 8 and reps % 2 == 0:
            check_mark_text['text']+=CHECK_MARK

# ---------------------------- UI SETUP ------------------------------- #


from tkinter import *

img = 'tomato.png'
window = Tk()
window.title("Pomodaro")
window.config(padx=100,pady=100,bg=YELLOW)

tomato = PhotoImage(file='tomato.png')
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(100,112,image=tomato)
text_Timer = canvas.create_text(100,130,fill='white',text="00:00",font=(FONT_NAME,24,'bold'))
canvas.grid(column=1,row=1)



timer_text = Label(text='Timer',font=(FONT_NAME,50,'bold'),fg='cyan',bg=YELLOW)
timer_text.grid(column=1,row=0)

start_btn = Button(text='Start',width=8,bg='pink',command=start_countDown)
start_btn.grid(column=0,row=2)

reset_btn = Button(text='Reset',width=8,bg='pink',command=reset_timer)
reset_btn.grid(column=2,row=2)

check_mark_text = Label(fg='green',bg=YELLOW)
check_mark_text.grid(row=4,column=1)


window.mainloop()