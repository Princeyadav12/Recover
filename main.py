from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory
import tkinter.messagebox as tmsg
import helper1 as he

color_one = "orange"
color_two = "white"

helvita = ("Helvetica", 15,"bold")

great = ("Helvetica", 40,"bold")

def open_file():
    global srcpath
    srcpath = askopenfilename(filetypes=[("raw files", "*.raw")])
    if srcpath == "" or srcpath == "()":
        pass
        #lbl = Label(window, text = f"Source {srcpath}",font = helvita, bg = "green").pack()
        # Button(window, text = "Start",font = helvita, bg = "orange", command = start_pro).pack(pady = 100)

def close_file():
    global srcpath
    srcpath = ""
    msg = "File is Unselected"
    tmsg.showinfo("Unselect", msg)

def start_pro():
    if (srcpath == "" or srcpath == "()"):
        msg = "No Source File is Selected"
        tmsg.showinfo("Recovered", msg)
    elif (destpath == "" or destpath == "()") :
        msg = "No Destination Folder is Selected"
        tmsg.showinfo("Recovered", msg)
    else: 
        print(srcpath)
        print(destpath)
        ans = he.recover(srcpath, destpath)
        msg = f"Total {ans} file recovered\nFile saved in {destpath} Directory"
        tmsg.showinfo("Recovered", msg)

def ask_dest():
    global destpath
    destpath = askdirectory()

def forget_dest():
    global destpath
    destpath = ""

def rate():
    msg = "Rate Us on Software Store"
    tmsg.showinfo("Rate us", msg)

def feedback():
    msg = "Sorry to hear that\nWrite us on princeydv1999@gmail.com"
    tmsg.showinfo("Feedback", msg)

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x500")
        # self.maxsize(800,500)
        self.minsize(800,500)
        self.title("Recover jpg photos by Prince")
        self.configure(background = color_one)
    

if __name__ == "__main__":
    global srcpath
    global destpath
    srcpath = ""
    destpath = ""
    window = GUI()
    menubar = Menu(window)

    m1 = Menu(menubar, tearoff = 0)
    m1.add_command(label = "Select Source File", font = helvita, command = open_file)
    m1.add_separator()
    m1.add_command(label = "Unselect Source File", font = helvita, command = close_file)
    m1.add_separator()
    m1.add_command(label = "Select Destination File", font = helvita, command = ask_dest)
    m1.add_separator()
    m1.add_command(label = "Unselect Destination File", font = helvita, command = forget_dest)
    window.config(menu = menubar)
    menubar.add_cascade(label="File",font = helvita, menu = m1)

    menubar.add_command(label = "Recover", font = helvita, command = start_pro)
    window.config(menu = menubar)

    m3 = Menu(menubar, tearoff = 0)
    m3.add_command(label = "Feedback", font = helvita, command = feedback)
    m3.add_separator()
    m3.add_command(label = "Rate Us", font = helvita, command = rate)
    window.config(menu = menubar)
    menubar.add_cascade(label="Rate", font = helvita, menu = m3)

    Label(window, text = "Welcome to Recover",bg = color_one, fg = "blue", font = great).pack()
    Label(window, text = "-Developed by Prince", bg = color_one, font = helvita).pack(padx = 10, anchor = 'e')
    
    
    photo = PhotoImage(file="logo.png")
    l1 = Label(image=photo)
    l1.pack()
    

    Label(window, text = "Quick Guide",bg = color_one, fg = "blue", font = great).pack(padx = 10,pady = (10,0), anchor='w')
    Label(window, text = "1.Select source file    File --> Select Source File",bg = color_one, font = helvita).pack(padx = 10, anchor = 'w')
    Label(window, text = "2.Select destination file    File --> Select Destination File", bg = color_one, font = helvita).pack(padx = 10, anchor = 'w')
    Label(window, text = "3.Click Start Button", bg = color_one, font = helvita).pack(padx = 10, anchor = 'w')

    menubar.add_command(label = "Exit", font = helvita, command = exit)
    window.config(menu = menubar)
    
    window.mainloop()