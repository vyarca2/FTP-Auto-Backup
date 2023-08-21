import os
from tkinter import *
from tkinter import ttk

scriptdir=os.path.dirname(os.path.abspath(__file__))
os.chdir(scriptdir)

win=Tk()
win.geometry("900x600")

label1=Label(win,text="Enter path",font=("Courier 12 bold"))
label1.pack()
def display_text1():
   global entry1
   path=entry1.get()
   filename1=open("directory.txt","w")
   filename1.write(path)
   inlabel1.configure(text=path)
inlabel1=Label(win,text="",font=("Courier 12 bold"))
inlabel1.pack()
entry1=Entry(win,width= 40)
entry1.focus_set()
entry1.pack()
ttk.Button(win,text="Okay",width=20,command=display_text1).pack(pady=20)

label2=Label(win,text="Enter server IP",font=("Courier 12 bold"))
label2.pack()
def display_text2():
   global entry2
   sip=entry2.get()
   filename2=open("serverip.txt","w")
   filename2.write(sip)
   inlabel2.configure(text=sip)
inlabel2=Label(win,text="",font=("Courier 12 bold"))
inlabel2.pack()
entry2=Entry(win,width=40)
entry2.focus_set()
entry2.pack()
ttk.Button(win,text="Okay",width=20,command=display_text2).pack(pady=20)

label3=Label(win,text="Enter username",font=("Courier 12 bold"))
label3.pack()
def display_text3():
   global entry3
   usn=entry3.get()
   filename3=open("username.txt","w")
   filename3.write(usn)
   inlabel3.configure(text=usn)
inlabel3=Label(win,text="",font=("Courier 12 bold"))
inlabel3.pack()
entry3=Entry(win,width= 40)
entry3.focus_set()
entry3.pack()
ttk.Button(win,text="Okay",width=20,command=display_text3).pack(pady=20)

label4=Label(win,text="Enter password",font=("Courier 12 bold"))
label4.pack()
def display_text4():
   global entry4
   pword=entry4.get()
   filename4=open("password.txt","w")
   filename4.write(pword)
   inlabel4.configure(text=pword)
inlabel4=Label(win,text="",font=("Courier 12 bold"))
inlabel4.pack()
entry4=Entry(win, width= 40)
entry4.focus_set()
entry4.pack()
ttk.Button(win,text="Okay",width=20,command=display_text4).pack(pady=20)

win.mainloop()
