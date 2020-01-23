from tkinter import *
import tkinter.messagebox as t
from tkinter import ttk
import tkinter as tK

tk = Tk()
tk.title("TicTacToe")
txt = ""

isCross = True;
turns = 0


def main():
    global btn1, btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9

    lbl = Label(tk, text="TicTacToe", font=("Arial", 20)).grid(row=0, column=1)

    btn1 = Button(tk, text=" ", font='Arial 40 bold', bg='black', fg='white', height=2, width=6,
                     command=lambda: box(btn1))
    btn1.grid(row=3, column=0)

    btn2 = Button(tk, text=' ', font='Arial 40 bold', bg='black', fg='white', height=2, width=6,
                     command=lambda: box(btn2))
    btn2.grid(row=3, column=1)

    btn3 = Button(tk, text=' ', font='Arial 40 bold', bg='black', fg='white', height=2, width=6,
                     command=lambda: box(btn3))
    btn3.grid(row=3, column=2)

    btn4 = Button(tk, text=' ', font='Arial 40 bold', bg='black', fg='white', height=2, width=6,
                     command=lambda: box(btn4))
    btn4.grid(row=4, column=0)

    btn5 = Button(tk, text=' ', font='Arial 40 bold', bg='black', fg='white', height=2, width=6,
                     command=lambda: box(btn5))
    btn5.grid(row=4, column=1)

    btn6 = Button(tk, text=' ', font='Arial 40 bold', bg='black', fg='white', height=2, width=6,
                     command=lambda: box(btn6))
    btn6.grid(row=4, column=2)

    btn7 = Button(tk, text=' ', font='Arial 40 bold', bg='black', fg='white', height=2, width=6,
                     command=lambda: box(btn7))
    btn7.grid(row=5, column=0)

    btn8 = Button(tk, text=' ', font='Arial 40 bold', bg='black', fg='white', height=2, width=6,
                     command=lambda: box(btn8))
    btn8.grid(row=5, column=1)

    btn9 = Button(tk, text=' ', font='Arial 40 bold', bg='black', fg='white', height=2, width=6,
                     command=lambda: box(btn9))
    btn9.grid(row=5, column=2)

    menubar = Menu(tk)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New Game", command=reset)
    filemenu.add_command(label="Exit", command=tk.quit)
    menubar.add_cascade(label="Game", menu=filemenu)

    tk.config(menu=menubar)

    tk.mainloop()


def highlightWinningCombo(button1, button2, button3):
    button1.config(bg="green")
    button2.config(bg="green")
    button3.config(bg="green")


def disableAll():
    for i in range(1,10):
        eval('btn' + str(i)).config(state='disabled')


def checkforwin():
    global txt
    if (btn1['text'] == 'X' and btn2['text'] == 'X' and btn3['text'] == 'X' or
            btn4['text'] == 'X' and btn5['text'] == 'X' and btn6['text'] == 'X' or
            btn7['text'] == 'X' and btn8['text'] == 'X' and btn9['text'] == 'X' or
            btn1['text'] == 'X' and btn5['text'] == 'X' and btn9['text'] == 'X' or
            btn3['text'] == 'X' and btn5['text'] == 'X' and btn7['text'] == 'X' or
            btn1['text'] == 'X' and btn2['text'] == 'X' and btn3['text'] == 'X' or
            btn1['text'] == 'X' and btn4['text'] == 'X' and btn7['text'] == 'X' or
            btn2['text'] == 'X' and btn5['text'] == 'X' and btn8['text'] == 'X' or
            btn3['text'] == 'X' and btn6['text'] == 'X' and btn9['text'] == 'X'):

        if btn1['text'] == 'X' and btn2['text'] == 'X' and btn3['text'] == 'X':
            highlightWinningCombo(btn1, btn2, btn3)

        if btn4['text'] == 'X' and btn5['text'] == 'X' and btn6['text'] == 'X':
            highlightWinningCombo(btn4, btn5, btn6)
        if btn7['text'] == 'X' and btn8['text'] == 'X' and btn9['text'] == 'X':
            highlightWinningCombo(btn7, btn8, btn9)
        if btn1['text'] == 'X' and btn5['text'] == 'X' and btn9['text'] == 'X':
            highlightWinningCombo(btn1, btn5, btn9)
        if btn3['text'] == 'X' and btn5['text'] == 'X' and btn7['text'] == 'X':
            highlightWinningCombo(btn3, btn5, btn7)
        if btn1['text'] == 'X' and btn4['text'] == 'X' and btn7['text'] == 'X':
            highlightWinningCombo(btn1, btn4, btn7)
        if btn2['text'] == 'X' and btn5['text'] == 'X' and btn8['text'] == 'X':
            highlightWinningCombo(btn2, btn5, btn8)
        if btn3['text'] == 'X' and btn6['text'] == 'X' and btn9['text'] == 'X':
            highlightWinningCombo(btn3, btn6, btn9)
        txt="Player 1 wins!!"
        disableAll()
        popup_bonus()

    elif(btn1['text'] == 'O' and btn2['text'] == 'O' and btn3['text'] == 'O' or
          btn4['text'] == 'O' and btn5['text'] == 'O' and btn6['text'] == 'O' or
          btn7['text'] == 'O' and btn8['text'] == 'O' and btn9['text'] == 'O' or
          btn1['text'] == 'O' and btn5['text'] == 'O' and btn9['text'] == 'O' or
          btn3['text'] == 'O' and btn5['text'] == 'O' and btn7['text'] == 'O' or
          btn1['text'] == 'O' and btn2['text'] == 'O' and btn3['text'] == 'O' or
          btn1['text'] == 'O' and btn4['text'] == 'O' and btn7['text'] == 'O' or
          btn2['text'] == 'O' and btn5['text'] == 'O' and btn8['text'] == 'O' or
          btn3['text'] == 'O' and btn6['text'] == 'O' and btn9['text'] == 'O'):

        if btn1['text'] == 'O' and btn2['text'] == 'O' and btn3['text'] == 'O':
            highlightWinningCombo(btn1, btn2, btn3)

        if btn4['text'] == 'O' and btn5['text'] == 'O' and btn6['text'] == 'O':
            highlightWinningCombo(btn4, btn5, btn6)
        if btn7['text'] == 'O' and btn8['text'] == 'O' and btn9['text'] == 'O':
            highlightWinningCombo(btn7, btn8, btn9)
        if btn1['text'] == 'O' and btn5['text'] == 'O' and btn9['text'] == 'O':
            highlightWinningCombo(btn1, btn5, btn9)
        if btn3['text'] == 'O' and btn5['text'] == 'O' and btn7['text'] == 'O':
            highlightWinningCombo(btn3, btn5, btn7)
        if btn1['text'] == 'O' and btn4['text'] == 'O' and btn7['text'] == 'O':
            highlightWinningCombo(btn1, btn4, btn7)
        if btn2['text'] == 'O' and btn5['text'] == 'O' and btn8['text'] == 'O':
            highlightWinningCombo(btn2, btn5, btn8)
        if btn3['text'] == 'O' and btn6['text'] == 'O' and btn9['text'] == 'O':
            highlightWinningCombo(btn3, btn6, btn9)
        txt = "Player 2 wins!!"
        disableAll()
        popup_bonus()

    elif turns == 9:
        txt = "It's a tie!!"
        popup_bonus()

    else:
        return False


def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func


def popup_bonus():
    global txt
    win = tK.Toplevel()
    win.wm_title("Result")

    l = tK.Label(win, text=txt, font='Arial 20 bold')
    l.grid(row=0, column=0)

    b = ttk.Button(win, text="Play Again..", command = combine_funcs(win.destroy, reset))
    b.grid(row=1, column=0)

    q =ttk.Button(win, text="Quit", command = combine_funcs(tk.quit, reset))
    q.grid(row=1, column=1)


def box(btn):
    global isCross, turns
    if isCross:
        btn.config(text="X")
        btn.configure(state=DISABLED)
        isCross = False
        turns += 1

    else:
        btn.config(text="O")
        btn.configure(state=DISABLED)
        isCross = True
        turns += 1

    checkforwin()


def reset():
    global turns,isCross
    turns = 0
    isCross = True
    for i in range(1,10):
        eval('btn'+str(i)).config(text = "")
        eval('btn' + str(i)).config(state='normal')
        eval('btn' + str(i)).config(bg = "black")


if __name__ == '__main__':
    main()

