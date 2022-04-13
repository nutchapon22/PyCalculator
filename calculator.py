from tkinter import *
def clear():
    global ex
    global showlek
    result = ""
    ex = ""
    showlek.set(result)
def press(num):
    global ex
    global showlek
    ex = ex + num
    showlek.set(ex)
def eq():
    try :
        global ex
        global showlek
        result = str(eval(ex))  
        showlek.set(result) 
    except:
        result ="Error"
        ex = ""
        showlek.set(result)
M = Tk()
M.option_add("*font","consolas 30")
showlek = StringVar()
ex = ""
M.title("เครื่องคิดเลข")
Mitor = Entry(M,textvariable=showlek)
Mitor.grid(row=0,column=0,columnspan=4)
CB = Button(M,text="Clear",command=clear)
CB.grid(row=1,column=0,columnspan=4,sticky="news")
#7-8-9-/
b7 = Button(M,text="7",command=lambda: press("7"))
b7.grid(row=2,column=0,sticky="news")
b8 = Button(M,text="8",command=lambda: press("8"))
b8.grid(row=2,column=1,sticky="news")
b9 = Button(M,text="9",command=lambda: press("9"))
b9.grid(row=2,column=2,sticky="news")
bh = Button(M,text="÷",command=lambda: press("/"))
bh.grid(row=2,column=3,sticky="news")
#4-5-6-*
b4 = Button(M,text="4",command=lambda: press("4"))
b4.grid(row=3,column=0,sticky="news")
b5 = Button(M,text="5",command=lambda: press("5"))
b5.grid(row=3,column=1,sticky="news")
b6 = Button(M,text="6",command=lambda: press("6"))
b6.grid(row=3,column=2,sticky="news")
bx = Button(M,text="X",command=lambda: press("*"))
bx.grid(row=3,column=3,sticky="news")
#1-2-3--
b1 = Button(M,text="1",command=lambda: press("1"))
b1.grid(row=4,column=0,sticky="news")
b2 = Button(M,text="2",command=lambda: press("2"))
b2.grid(row=4,column=1,sticky="news")
b3 = Button(M,text="3",command=lambda: press("3"))
b3.grid(row=4,column=2,sticky="news")
bl = Button(M,text="-",command=lambda: press("-"))
bl.grid(row=4,column=3,sticky="news")
#0-.-+
b0 = Button(M,text="0",command=lambda: press("0"))
b0.grid(row=5,column=0,sticky="news")
bdot = Button(M,text=".",command=lambda: press("."))
bdot.grid(row=5,column=1,columnspan=2,sticky="news")
bp = Button(M,text="+",command=lambda: press("+"))
bp.grid(row=5,column=3,sticky="news")
# =
tawkub = Button(M,text="=",command=eq)
tawkub.grid(row=6,column=0,columnspan=4,sticky="news")
M.mainloop()
