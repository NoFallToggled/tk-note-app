# TODO: center the packed labels
# TODO: add separator between labels
from tkinter import *
from tkinter import ttk

# setting the window up
root = Tk()
scrw, scrh = root.winfo_screenwidth(), root.winfo_screenheight()
root.title('super duper unfunctonial note app')
root.geometry('500x500-{}+{}'.format(int(scrw/2-250), int(scrh/2-270)))
root.resizable(False, False)
# ---------------------

# setting images
eyeon = PhotoImage(file = 'tk_imgs/eyeon.png',)
eyeoff = PhotoImage(file = 'tk_imgs/eyeoff.png',)
# ------------

# setting background
bckgrnd = Label(text='', background='#1e1e1e') 
bckgrnd.place(x=206, y=0, width=294 ,height=500)
# ------------

# gets the width of the text inside entry bar
def get_width():
    label = Label(root, text=entxt.get())
    label.place(x=0, y=-100)
    root.update_idletasks()
    width = label.winfo_width()
    label.destroy()
    return width
# -------------------------------------

def move_buttons(way=''):
    if way == 'down':
        sbutton.place(y=57)
        dbutton.place(y=92)
        showtxt.place(y=57)
    elif way == 'up':
        sbutton.place(y=35)
        dbutton.place(y=70)
        showtxt.place(y=35)
    else:
        print('move_buttons function got wrong variable')



limit = 0
ycord = 0
labels_list = []
def svtxt():
    global ycord, limit
    if limit < 22:
        if entxt.get():
            width = get_width()
            label = Label(root, text=entxt.get(), bg='#1e1e1e')

            if width > 285:
                pass
            else:
                label.place(x=213, y=ycord)
                labels_list.append(label)
                ycord += 22
                limit += 1
    else:
        warning.config(text='Warning: limit is reached')
        move_buttons('down')

def dlttxt():
    global labels_list
    global ycord
    global limit
    '''this function has to
    delete all the packed labels
    '''
    while len(labels_list) != 0:
        cur_label = labels_list.pop()
        cur_label.place_forget()
        cur_label.destroy()
        ycord = 0
        limit = 0
        warning.config(text='')
        move_buttons('up')


onoff = True
def chngtxt():
    global onoff
    if onoff:
        entry.config(show='*')
        showtxt.config(image=eyeoff, text='show')
        onoff = False
    else:
        entry.config(show='')
        showtxt.config(image=eyeon, text='hide')
        onoff = True


warning = Label(root, text='', fg='yellow')
warning.place(x=25, y=33)
def wrnng(var, index, mode):
    width = get_width()
    if width > 285:
        warning.config(text='Warning: text too long')
        move_buttons('down')
    else:
        if limit != 22: 
            warning.config(text='')
            move_buttons('up')
        else:
            warning.config(text='Warning: limit is reached')
            move_buttons('down')
        
               

# setting entry widget
entxt = StringVar()
entry = Entry(root, borderwidth=4, textvariable=entxt, show='')
entxt.trace('w', wrnng)
entry.place(x=0, y=0) 
entry.focus()
# ------------

# setting show text button
showtxt = Button(root, command=chngtxt, pady=5, image=eyeon, text='hide', compound='top', width=40)
showtxt.place(x=150, y=35)
# ------------

#  setting save text button
sbutton = Button(root, text='save text', command=svtxt)
sbutton.place(x=50, y=35)
# ------------

# setting delete text button
dbutton = Button(root, text='Delete all', command=dlttxt)
dbutton.place(x=49, y=70)
# ------------

# setting seperator widget
separator = ttk.Separator(root, orient='vertical')
separator.place(x=206, y=0, height=500)
# ------------


root.mainloop()