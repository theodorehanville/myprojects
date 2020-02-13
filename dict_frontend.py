from tkinter import *
import dict_backend

def search_command():
    list.delete(0,END)
    for row in dict_backend.dictionary(e1_str.get()):
        list.insert(END,row)


window = Tk()

e1_str = StringVar()
e1 = Entry(window, textvariable = e1_str)
e1.grid(row = 0, column = 0)

b1 = Button(window, text = "Search",command = search_command)
b1.grid(row=0, column = 1)

l1 = Label(window,text = " ")
l1.grid(row =1,column = 1)

list = Listbox(window,height = 6,width = 35)
list.grid(row = 2,column =0,rowspan = 5,columnspan=2 )









window.mainloop()
