BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ('Ariel',40,'italic')
WORD_FONT = ('Ariel',60,'bold')
from tkinter import *
import pandas as pd
import random
chosen_word = NONE
##################
""" it changes csv into dict by putting coulmn name then its value then 
#another coulmn name and value and put 1 row as a dict
func name DataFrame.to_dict()"""

######################################
# read data from csv file
try:
    df = pd.read_csv('-/data/words_to_learn.csv')
    words_list = df.to_dict(orient="records")
except FileNotFoundError:
    df = pd.read_csv('./data/french_words.csv')
    words_list = df.to_dict(orient="records")

###########################################
#generate the random word
def generate_random_Word():
    word_from_dict = random.choice(words_list)
    global chosen_word,flip_timer
    flip_timer = window.after_cancel(flip_timer)
    chosen_word = word_from_dict
    canvas.itemconfigure(tagOrId=img_canvas,image=card_front_img)
    canvas.itemconfigure(title,text='French',fill='black')
    canvas.itemconfigure(tagOrId=word,text=word_from_dict['French'],fill='black')
    flip_timer = window.after(3000,flip_card)

#############################################
# flip card
def flip_card():
    canvas.itemconfigure(title,text='English',fill='white')
    canvas.itemconfigure(tagOrId=word,text=chosen_word['English'],fill='white')
    canvas.itemconfigure(tagOrId=img_canvas,image=card_back_img)
################################################
# check if word is learnt
def words_to_learn():
    words_list.remove(chosen_word)
    df22 = pd.DataFrame(words_list)
    df22.to_csv('data/words_to_learn.csv',index=False)
    generate_random_Word()

    
################################################
window = Tk()

window.title('Flashy')
window.config(background=BACKGROUND_COLOR,padx=50,pady=50)

# timer that flip card
flip_timer = window.after(3000,flip_card)

canvas = Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)

card_back_img = PhotoImage(file=r'F:\python course practice\Day 31\images\card_back.png')
card_front_img = PhotoImage(file=r'F:\python course practice\Day 31\images\card_front.png')
img_canvas = canvas.create_image(400,250,image=card_front_img,)

title = canvas.create_text(400,150,text='Title',font=TITLE_FONT,)
word = canvas.create_text(400,263,text='Word',font=WORD_FONT,)

canvas.grid(row=0,column=0,columnspan=2)



#Buttons
right_img = PhotoImage(file=r'F:\python course practice\Day 31\images\right.png')
right_btn = Button(image=right_img,highlightthickness=0,command=words_to_learn)
right_btn.grid(row=1,column=0)

wrong_img = PhotoImage(file=r'F:\python course practice\Day 31\images\wrong.png')
wrong_btn = Button(image=wrong_img,highlightthickness=0,command=generate_random_Word)
wrong_btn.grid(row=1,column=1)


generate_random_Word()
window.mainloop()

"""
#labels

 title_label = Label(text='Title',font=TITLE_FONT,fg='white',highlightthickness=0,bg=BACKGROUND_COLOR)
title_label.place(x=350,y=150)

word_label = Label(text='Word',font=WORD_FONT,fg='white',highlightthickness=0,bg=BACKGROUND_COLOR)
word_label.place(x=310,y=263) 
This time use canvas text built-in"""