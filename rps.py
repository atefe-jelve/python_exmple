from faulthandler import disable
from itertools import count
from sre_parse import State
import tkinter as tk
from tkinter import ttk
import random
from tkinter import N,S,W,E
from webbrowser import BackgroundBrowser
window = tk.Tk()

list_of_score_user = []
list_of_score_ai = []
list_select = ['Rock' , 'Paper' ,'Scissors']
count_play = 0

window.title('Game : Rock , Paper ,Scissors')
window.geometry("600x400")

ai_lbl = tk.Label(
    window,
    width=30,
    height=10,
    text = 'Ai choice',
    background='pink'
)
user_lbl = tk.Label(
    window,
    width=30,
    height=10,
    text = 'User choice',
    background='pink'
)
result_lbl = tk.Label(
    window,
    width=30,
    height=5,
    text = 'Resutl Game',
    background='white'
)

def select_rock():
        user_lbl['text'] = rock_btm['text']
        result  = start_game(user_lbl['text'])
        if result == False:
            rock_btm['state'] = 'disable'
            paper_btm['state'] = 'disable'
            scissors_btm['state'] = 'disable'
def select_paper():
        user_lbl['text'] = paper_btm['text']
        result = start_game(user_lbl['text'])
        if result == False:
            rock_btm['state'] = 'disable'
            paper_btm['state'] = 'disable'
            scissors_btm['state'] = 'disable'
def select_scissors():
        user_lbl['text'] = scissors_btm['text']
        result = start_game(user_lbl['text'])
        if result == False:
            rock_btm['state'] = 'disable'
            paper_btm['state'] = 'disable'
            scissors_btm['state'] = 'disable'

rock_btm = ttk.Button(
    window,
    width=20, 
    text='Rock',
    command=select_rock,
    # state='disable'
)
paper_btm = ttk.Button(
    window,
    width=20,
    text='Paper',
    command=select_paper,
)
scissors_btm = ttk.Button(
    window,
    width=20,
    text='Scissors',
    command=select_scissors,
)
def start_game(user_select):
    while count_play > 0:
        while True:
            ai_lbl['text'] = random.choice(list_select)
            if ai_lbl['text'] == 'Rock' and user_select == 'Paper' or \
                ai_lbl['text'] == 'Paper' and user_select == 'Scissors' or \
                    ai_lbl['text'] == 'Scissors' and user_select == 'Rock':
                list_of_score_user.append(10)
                result_lbl['text'] = f'You get "10"  sum of score is :{sum(list_of_score_user)} '
                if count_play >= 0:
                    count_play -= 1
                    return
                return False
            elif ai_lbl['text'] == user_select:
                result_lbl['text'] = 'Tie'
                return True
            else:
                list_of_score_ai.append(10)
                result_lbl['text'] = f'Ai get "10" sum of score is :{sum(list_of_score_ai)}'
                if count_play >= 0:
                    count_play -= 1
                    return
                return False


ai_lbl.grid(row=0 , column=0)
user_lbl.grid(row=0 , column=2)
result_lbl.grid(row=1, column=0,columnspan=3,sticky=(E,W))
rock_btm.grid(row=2, column=0,sticky=(N,S))
# rock_btm.place(height=50)
paper_btm.grid(row=2, column=1,sticky=(N,S))
scissors_btm.grid(row=2, column=2,sticky=(N,S))

dict_of_select = {
}

window.mainloop()
