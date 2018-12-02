from tkinter import *
import tkinter.messagebox
import datetime
import  sqlite3
import mypdf
from mypdf import user_pass
###############################FOR SENDING MAIL######################
#import smtplib
#server=smtplib.SMTP("smtp.gmail.com",587)
#server.starttls()
#server.login("amandudeja2@gmail.com","iamrobotman@12")
#sender="amandudeja2@gmail.com"
#################################################################################################
from subprocess import call



conn=sqlite3.connect("VISITORDB.db")
mydb=conn.cursor()
emp=sqlite3.connect("EMPLOYEES.db")
emdb=emp.cursor()

def restart():
	root.destroy()
	call(["python", "final_conclusion.py", ""])





root = Tk()
root.title('Visitor Management Application')
root.geometry("1200x720+0+0")
root.resizable(False,False)
##CREATING FRAMES
#frame1 = Frame(root, bg="#E2C499", height=720, width=1200)
#frame1.pack(side=LEFT,fill=BOTH)
frame2=Frame(root, bg="#E2C499", height=720, width=1200)
frame2.pack(side=LEFT,fill=BOTH)
frame3 = Frame(root, height=720, width=1200, bg='#E2C499')
frame3.pack(side=LEFT,fill=BOTH)
canvas = Canvas(root, width=1200, height=720,bg='#E2C499')
canvas.pack(side=LEFT)
frame5=Frame(root,bg="#E2C499",height=720,width=1200)
frame5.pack(side=LEFT,fill=BOTH)


#################################################MAIN PROGRAM##################################################################################################################

def frame_2():
        

    ############widgets for second frame#############################3

    button1 = Button(frame2, text="Visitor's Entry",bd=10, bg='#E8A735', fg='#8C0004',command=cal_third_frame)

    button1.config(font=('arial black', 40, 'bold'))
    button1.place(x=100, y=50)
    button2 = Button(frame2, text="Visitor's Exit", bd=10, bg='#E8A735', fg='#8C0004',command=cal_fifth_frame)
    button2.config(font=('arial black', 40, 'bold'))
    button2.place(x=100, y=250)
    button3 = Button(frame2, text="Show Visitors", bd=10, bg='#E8A735', fg='#8C0004',command=cal_fourth_frame)
    button3.config(font=('arial black', 40, 'bold'))
    button3.place(x=100, y=450)
    button4 = Button(frame2, text="QUIT", bd=10, bg='#E8A735', fg='#8C0004',command=root.destroy)
    button4.config(font=('arial black', 20, 'bold'))
    button4.place(x=600, y=600)
    label = Label(frame2, text="Welcome\n To The\n Visitor Management\n Application", bg="#E2C499",fg="#8C0004")
    label.config(font=('monotypecorsiva', 40, 'bold italic '))
    label.place(x=650, y=100)

def frame_3():
################widgets for frame 3################################

    label = Label(frame3, text="Visitor's Details", bg='#E2C499', fg='#8C0004')
    label.config(font=("arial black", 30, 'bold'))
    label.place(x=600, y=0)
##############GETTING ID#################
    #label2 = Label(frame3, text="Visitor Id", bg='gray83', fg='salmon')
    #label2.config(font=("arial black", 30, 'bold'))
    #label2.place(x=100, y=75)
    #entry1 = Entry(frame3, bd=7, width=50)
    #entry1.place(x=600, y=75)
#############GETTING NAME#################
    labe3 = Label(frame3, text="Name", bg='#E2C499', fg='#8C0004')
    labe3.config(font=("arial black", 30, 'bold'))
    labe3.place(x=100, y=150)
    entry2 = Entry(frame3, bd=7, width=50)
    entry2.place(x=600, y=150)
#########GETTING MOBILE NUMBER##################
    label4 = Label(frame3, text="Mobile No.", bg='#E2C499', fg='#8C0004')
    label4.config(font=("arial black", 30, 'bold'))
    label4.place(x=100, y=225)
    entry3 = Entry(frame3, bd=7, width=50)
    entry3.place(x=600, y=225)
#########GETTING DATE AND TIME#########################
    label5 = Label(frame3, text="Date & Time", bg='#E2C499', fg='#8C0004')
    label5.config(font=("arial black", 30, 'bold'))
    label5.place(x=100, y=300)
    entry4 = Entry(frame3, bd=7, width=50)
    entry4.insert(END, datetime.datetime.now().strftime('%d/%m/%y  %H:%M:%S'))
    entry4.configure(state="readonly")
    entry4.place(x=600, y=300)
############GETTING ADDRESS#####################
    label6 = Label(frame3, text="Address", bg='#E2C499', fg='#8C0004')
    label6.config(font=("arial black", 30, 'bold'))
    label6.place(x=100, y=375)
    entry5 = Entry(frame3, bd=7, width=50)
    entry5.place(x=600, y=375)
#######GETTING PURPOSE##############
    label7 = Label(frame3, text="Purpose Of Visit", bg='#E2C499', fg='#8C0004')
    label7.config(font=("arial black", 30, 'bold'))
    label7.place(x=100, y=450)
    entry6 = Entry(frame3, bd=7, width=50)
    entry6.place(x=600, y=450)
#########GETTING PERSON TO MEET################
    label8 = Label(frame3, text="Whom to Meet ", bg='#E2C499', fg='#8C0004')
    label8.config(font=("arial black", 30, 'bold'))
    label8.place(x=100, y=525)
    entry7 = Entry(frame3, bd=7, width=50)
    entry7.place(x=600, y=525)

##############FUNCTION TO CHECK ENTRY###################
    def check():
        #a = entry1.get()
        b = entry2.get()
        c = entry3.get()
        d = entry4.get()
        e = entry5.get()
        f = entry6.get()
        g = entry7.get()

        if  b == "" or c == "" or d=="" or e == "" or f == "" or g == "":
                
            tkinter.messagebox.showinfo("WARNING!", "Please Fill The Form")
        else:
                emdb.execute("SELECT email from list where name=?",(g,))
                rows=emdb.fetchone()
                if rows:
                        message="Subject: {}\n\n{}".format("NEW VISITOR","You Have a Visitor In Building\n  Name: "+str(b.title())+" \n For "+str(f.title())+" purpose")
                        print(message)
                        sql = "INSERT INTO 'details' (name,mobile,date_time,address,purpose,whom) VALUES( ?, ?, ?, ?, ?, ?)"
                        mydb.execute(sql , ( b, c, d, e, f, g))
                        conn.commit()
                        lastentquery="SELECT id FROM details ORDER BY id DESC LIMIT 1"
                        mydb.execute(lastentquery)
                        id_preview=mydb.fetchone()
                        idlist=list(id_preview)
                        tkinter.messagebox.showinfo("INFORMATION","DETAILS FOR " + "\n ID \t" + str(idlist[0]) + "\n NAME \t" + str(b) + "\n HAVE BEEN ADDED")
                        c=mypdf.user_pass(str(idlist[0]),f,b)
                        #receiver=rows
                        #server.sendmail(sender,receiver,message)
                        #server.close()
######################reset entry fields#########################
            #entry1.delete(0, "end")
                        entry2.delete(0, "end")
                        entry3.delete(0, "end")
                        entry5.delete(0, "end")
                        entry6.delete(0, "end")
                        entry7.delete(0, "end")
                else:
                        tkinter.messagebox.showinfo("SORRY!","NO SUCH EMPLOYEE")
                        entry2.delete(0, "end")
                        entry3.delete(0, "end")
                        entry5.delete(0, "end")
                        entry6.delete(0, "end")
                        entry7.delete(0, "end")
                        




    button = Button(frame3, text="Add Visitor", command=check,bg='#E8A735',fg='#8C0004')
    button.config(font=("monotype corsiva", 20, "bold"))
    button.place(x=600, y=600)
    button3=Button(frame3,text="BACK",command=restart,bg='#E8A735',fg='#8C0004')
    button3.config(font=("monotype corsiva", 20, "bold"))
    button3.place(x=900,y=600)

############widgets for frame4################################33
def frame_4():

    scrollbary = Scrollbar(root, command=canvas.yview)
    scrollbary.pack(side=RIGHT, fill=Y)

    canvas.configure(yscrollcommand=scrollbary.set)
    canvas.configure(scrollregion=(0, 0, 10000, 10000))

    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas

    frame4 = Frame(canvas, bg='#E2C499')
    canvas.create_window((0, 0), window=frame4, anchor='nw')
    mydb.execute("SELECT * FROM details")
    rows = mydb.fetchall()
    
    conn.commit()



    label1 = Label(frame4, text="VISITOR ID",bg='#E2C499',fg='#8C0004')
    label1.config(font=("TIMES NEW ROMAN", 15,"bold"))
    label1.grid(row=0, column=0, padx=3, pady=5)
    label2 = Label(frame4, text="NAME",bg='#E2C499',fg='#8C0004')
    label2.config(font=("TIMES NEW ROMAN", 15, "bold"))
    label2.grid(row=0, column=1, padx=3, pady=5)
    label3 = Label(frame4, text="MOBILE NO",bg='#E2C499',fg='#8C0004')
    label3.config(font=("TIMES NEW ROMAN", 15, "bold"))
    label3.grid(row=0, column=2, padx=3, pady=5)
    label4 = Label(frame4, text="DATE&TIME",bg='#E2C499',fg='#8C0004')
    label4.config(font=("TIMES NEW ROMAN", 15, "bold"))
    label4.grid(row=0, column=3, padx=3, pady=5)
    label5 = Label(frame4, text="OUT_TIME",bg='#E2C499',fg='#8C0004')
    label5.config(font=("TIMES NEW ROMAN", 15, "bold"))
    label5.grid(row=0, column=4, padx=3, pady=5)
    label6 = Label(frame4, text="ADDRESS",bg='#E2C499',fg='#8C0004')
    label6.config(font=("TIMES NEW ROMAN", 15, "bold"))
    label6.grid(row=0, column=5, padx=3, pady=5)
    label7 = Label(frame4, text="PURPOSE OF VISIT",bg='#E2C499',fg='#8C0004')
    label7.config(font=("TIMES NEW ROMAN", 15, "bold"))
    label7.grid(row=0, column=6, padx=3, pady=5)
    label8 = Label(frame4, text="WHOMTO MEET",bg='#E2C499',fg='#8C0004')
    label8.config(font=("TIMES NEW ROMAN", 15, "bold"))
    label8.grid(row=0, column=7, padx=3, pady=5)
    button = Button(frame4, text="BACK", bd=5,width=20,command=cal_second_frame,bg='#E8A735', fg='#8C0004')
    button.config(font=("arialblack", 8, "bold"))
    button.grid(row=len(rows)+5,column=4,pady=2)


    #
    for j, i in enumerate(rows):
        
        Label(frame4, text=i[0],bg='#E2C499',fg='#C8000A').grid(column=0, row=j + 1, padx=5, pady=5)
        Label(frame4, text=i[1],bg='#E2C499',fg='#C8000A').grid(column=1, row=j + 1, padx=5, pady=5)
        Label(frame4, text=i[2],bg='#E2C499',fg='#C8000A').grid(column=2, row=j + 1, padx=5, pady=5)
        Label(frame4, text=i[3],bg='#E2C499',fg='#C8000A').grid(column=3, row=j + 1, padx=5, pady=5)
        Label(frame4, text=i[4],bg='#E2C499',fg='#C8000A').grid(column=4, row=j + 1, padx=5, pady=5)
        Label(frame4, text=i[5],bg='#E2C499',fg='#C8000A').grid(column=5, row=j + 1, padx=5, pady=5)
        Label(frame4, text=i[6],bg='#E2C499',fg='#C8000A').grid(column=6, row=j + 1, padx=5, pady=5)
        Label(frame4, text=i[7],bg='#E2C499',fg='#C8000A').grid(column=7, row=j + 1, padx=5, pady=5)
        
################widgets in frame5########################
def frame_5():

    label2 = Label(frame5, text="Visitor Id", bg='#E2C499',fg='#C8000A')
    label2.config(font=("arial black", 30, 'bold'))
    label2.place(x=100, y=75)
    entry1 = Entry(frame5, bd=7, width=50)
    entry1.place(x=600, y=75)

    def make_exit():
        out_time = datetime.datetime.now().strftime('%d/%m/%y  %H:%M:%S')
        a = out_time
        b = entry1.get()
        if b == "":
            restart()
        else:
            mydb.execute("Select * from details where id= ? ", (b,))
            result = mydb.fetchone()
            if result:
                update_outtime_query = "update details set OutTime= ? where id = ?"
                mydb.execute(update_outtime_query, (a, b))
                conn.commit()
                tkinter.messagebox.showinfo("INFORMATION", "DETAILS \n You made exit at  \t" + out_time + "\n Saved to DB")
                entry1.delete(0,"end")

                restart()
            else:
                tkinter.messagebox.showinfo("Error", "Visitor ID Not Found")
                entry1.delete(0, "end")
                cal_fifth_frame()


                #time.sleep(3)


    button = Button(frame5, text="Exit",command=make_exit,bg='#E8A735', fg='#8C0004')
    button.config(font=("arial", 20, "bold"))
    button.place(x=600, y=600)


#####################frame overlapping########################3
def cal_second_frame():
    frame5.pack_forget()
    canvas.pack_forget()
    frame3.pack_forget()
    #frame1.pack_forget()
    frame2.pack()

def cal_third_frame():
    frame2.pack_forget()
    frame3.pack()
def cal_fourth_frame():
    frame2.pack_forget()
    canvas.pack()
def cal_fifth_frame():
    frame2.pack_forget()
    frame5.pack()

###############call all frames and forget all except first##########################33
#frame_1()
frame_2()
frame_3()
frame_4()
frame_5()


frame5.pack_forget()
canvas.pack_forget()
frame3.pack_forget()


#############################################

root.mainloop()

