from tkinter import *
import tkinter.messagebox
import datetime
import  sqlite3
from subprocess import call



conn=sqlite3.connect("VISITORDB.db")
mydb=conn.cursor()





root = Tk()
root.title('Visitor Management Application')
root.geometry("1200x720+0+0")
root.resizable(False,False)
##CREATING FRAMES
frame1 = Frame(root, bg="#E2C499", height=720, width=1200)
frame1.pack(side=LEFT,fill=BOTH)

#################################################MAIN PROGRAM##################################################################################################################

def frame_1():
#############wigets for frame 1#####################
    label2 = Label(frame1, text="LOGIN", bg='#E2C499', fg="#8C0004")
    label2.config(font=('times new roman', 50, 'bold underline'))
    label2.place(x=550, y=0)
    photo = PhotoImage(file="barcodeindialimited.png")
    frame1.img = photo

    label1 = Label(frame1, image=photo, height=200, width=200, bd=10)
    label1.place(x=550, y=150)
    label3 = Label(frame1, text="PASSWORD", fg="#8C0004", bg="#E2C499")
    label3.config(font=("arial black", 15, "bold"))
    label3.place(x=500, y=400)
    e = Entry(frame1, bd=5, show="*")
    e.place(x=650, y=400)
#################check password#####################and calling next frame if true###################
    def check():
        PASSWORD = e.get()
        if PASSWORD == "admin":
            root.destroy()
            call(["python", "final_conclusion.py", ""])

            #print("cal_second_frame()")
        elif PASSWORD == "":
            tkinter.messagebox.showinfo("ALERT", "FILL THE PASSWORD")

        else:
            tkinter.messagebox.showinfo("WARNING", "WRONG PASSWORD")


    button = Button(frame1, text="Log In", command=check, bg='#E8A735', bd=5, fg="#8C0004")
    button.config(font=('monotype corsiva', 20, 'bold'))
    button.place(x=550, y=550)

frame_1()
root.mainloop()
