from tkinter import *

def btnclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnclear():
    global operator
    operator = ""
    text_Input.set("")

def btnequal():
    global operator
    result = str(eval(operator))
    text_Input.set(result)

cal = Tk()
cal.title("Calculator")
operator = ""
text_Input = StringVar()
txtDisplay = Entry(cal, width=30, font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4, bg='aqua', justify='right').grid(columnspan=4)

bt7 = Button(cal, padx=30, bd=8, fg="black", font=('arial', 20, 'bold'), text="7", bg="silver", command=lambda:btnclick(7)).grid(row=1, column=0)
bt8 = Button(cal, padx=30, bd=8, fg="black", font=('arial', 20, 'bold'), text="8", bg="silver", command=lambda:btnclick(8)).grid(row=1, column=1)
bt9 = Button(cal, padx=30, bd=8, fg="black", font=('arial', 20, 'bold'), text="9", bg="silver", command=lambda:btnclick(9)).grid(row=1, column=2)
btDe = Button(cal, padx=30, bd=8, fg="black", font=('arial', 20, 'bold'), text="/", bg="silver", command=lambda:btnclick("/")).grid(row=1, column=3)
#---------------------------------------------------------------------------------------------------------------------
bt4 = Button(cal, padx=30, bd=8, fg="black", font=('arial', 20, 'bold'), text="4", bg="silver", command=lambda:btnclick(4)).grid(row=2, column=0)
bt5 = Button(cal, padx=30, bd=8, fg="black", font=('arial', 20, 'bold'), text="5", bg="silver", command=lambda:btnclick(5)).grid(row=2, column=1)
bt6 = Button(cal, padx=30, bd=8, fg="black", font=('arial', 20, 'bold'), text="6", bg="silver", command=lambda:btnclick(6)).grid(row=2, column=2)
btMu = Button(cal, padx=30, bd=8, fg="black", font=('arial', 20, 'bold'), text="*", bg="silver", command=lambda:btnclick("*")).grid(row=2, column=3)
#---------------------------------------------------------------------------------------------------------------------
bt1 = Button(cal, padx=30, bd=8, fg="black", font=('arial', 20, 'bold'), text="1", bg="silver", command=lambda:btnclick(1)).grid(row=3, column=0)
bt2 = Button(cal, padx=30, bd=8, fg="black", font=('arial', 20, 'bold'), text="2", bg="silver", command=lambda:btnclick(2)).grid(row=3, column=1)
bt3 = Button(cal, padx=30, bd=8, fg="black", font=('arial', 20, 'bold'), text="3", bg="silver", command=lambda:btnclick(3)).grid(row=3, column=2)
btMi = Button(cal, padx=30, bd=8, fg="black", font=('arial', 20, 'bold'), text="-", bg="silver", command=lambda:btnclick("-")).grid(row=3, column=3)
#---------------------------------------------------------------------------------------------------------------------
btC = Button(cal, padx=30, bd=8, fg="black", font=('arial', 20, 'bold'), text="C", bg="silver", command=lambda:btnclear()).grid(row=4, column=0)
btDo = Button(cal, padx=30, bd=8, fg="black", font=('arial', 20, 'bold'), text=".", bg="silver", command=lambda:btnclick(".")).grid(row=4, column=1)
bt0 = Button(cal, padx=30, bd=8, fg="black", font=('arial', 20, 'bold'), text="0", bg="silver", command=lambda:btnclick(0)).grid(row=4, column=2)
btPl = Button(cal, padx=30, bd=8, fg="black", font=('arial', 20, 'bold'), text="+", bg="silver", command=lambda:btnclick("+")).grid(row=4, column=3)
#---------------------------------------------------------------------------------------------------------------------
btOp = Button(cal, padx=30, bd=8, fg="black", font=('arial', 20, 'bold'), text="(", bg="silver", command=lambda:btnclick("(")).grid(row=5, column=0)
btCl = Button(cal, padx=30, bd=8, fg="black", font=('arial', 20, 'bold'), text=")", bg="silver", command=lambda:btnclick(")")).grid(row=5, column=1)
btEq = Button(cal, padx=90, bd=8, fg="black", font=('arial', 20, 'bold'), text="=", bg="silver", command=lambda:btnequal()).grid(row=5, column=2, columnspan=2)
cal.mainloop()