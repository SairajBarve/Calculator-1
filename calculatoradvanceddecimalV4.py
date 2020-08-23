import tkinter
from tkinter import *
from tkinter import messagebox

#functions which runs the calculator

val = "" #for concatenating and displaying the keyboard inputs on the screen
A = 0 # assigning an integer value for performing the actions like addition/subtraction etc
operator =""

def btn_1_isclicked():
    global val 
    val = val + "1" 
    data.set(val) 

def btn_2_isclicked():
    global val
    val = val + "2"
    data.set(val)

def btn_3_isclicked():
    global val
    val = val + "3"
    data.set(val)

def btn_4_isclicked():
    global val
    val = val + "4"
    data.set(val)

def btn_5_isclicked():
    global val
    val = val + "5"
    data.set(val)

def btn_6_isclicked():
    global val
    val = val + "6"
    data.set(val)

def btn_7_isclicked():
    global val
    val = val + "7"
    data.set(val)

def btn_8_isclicked():
    global val
    val = val + "8"
    data.set(val)

def btn_9_isclicked():
    global val
    val = val + "9"
    data.set(val)

def btn_0_isclicked():
    global val
    val = val + "0"
    data.set(val)

#decimal button
def btn_decimal_isclicked():
    global val
    val = val + "."
    data.set(val)

#addition operator
def btn_plus_clicked():
    global A
    global operator
    global val
    A = float(val)
    operator = "+"
    val = val + " + "
    data.set(val)

#subtraction operator
def btn_minus_isclicked():
    global A
    global val
    global operator
    A = float(val)
    operator = "-"
    val = val + " - "
    data.set(val)

#Multiplication operator
def btn_multiply_isclicked():
    global A
    global val
    global operator
    A = float(val)
    operator = "*"
    val = val + " * "
    data.set(val)

#Division operator
def btn_division_isclicked():
    global A
    global val
    global operator
    A = float(val)
    operator = "/"
    val = val + " / "
    data.set(val)

#clear button
def btn_clear_isclicked():
    global A
    global val
    global operator
    val = ""
    A = 0
    operator =""
    data.set(val)
    data1.set(val)



#equal to button
def btn_equalto_isclicked():
    global A
    global val
    global operator
    val2 = val  
    if operator == "+":
        #store this string value as an integer
        x = float((val2.split("+")[1]))
        C = A + x
        val = str(C)
        data1.set(val)
#the problem here is that before user presses "=", there are already two values on the label and an operator between them,  so we go by splitting these two values on both sides of the operator
#the value gets split into two values in a list, first value in [0] and second in [1], the 0'th value is already in A (see in addition operator,"A = int(A)"")

    elif operator =="-":
        x = float((val2.split("-")[1]))
        C = A - x
        val= str(C)
        data1.set(val)

    elif operator =="*":
        x = float((val2.split("*")[1]))
        C = A * x
        C = round(C,2)#//////////// applying round() to decimal values
        val = str(C)
        data1.set(val)

    elif operator =="/":
        x = float((val2.split("/")[1]))
        
        if x == 0:
            messagebox.showerror("Error", "Jaison! Are you an idiot? Why will someone try to divide anything by 0?")
            val = ""
            A = 0
            data1.set(val)
        else:
            C= A / x
            C = round(C,2) #////////// i'm trying to round this number so we dont end up getting strage decimal values 21st august 5:28pm; It worked!!!!!! :D
            val = str(C)
            data1.set(val)
        #now how can we avoid scenario where user try dividing something with zero
         



root=tkinter.Tk()
root.geometry('250x500+300+300')
root.resizable(0,0) #not resizable
root.title("Jaison's Calculator 4.0") #title for the calculator


#this is the window where the results should appear ///////////////////////////////////

data1 = StringVar()
lbl1 = Label(root, text = "label1", anchor = SE, font = ("Verdana", 30), textvariable= data1, bg = "#4b5c6a", fg = "#ffffff", )
lbl1.pack(expand=True, fill="both")

#the place where the calculations are made
data = StringVar() #connecting the UI to a variable
lbl = Label(root, text ="Label", anchor = SE, font = ("Verdana", 20), textvariable = data, bg="#4b5c6a", fg="#ff9f0a", ) #textvariable is the connector
lbl.pack(expand="True", fill="both")

# Keyboard
# # All the 4 button rows 

btnrow1 =Frame(root,bg="#000000")
btnrow1.pack(expand=True, fill ="both")

btnrow2 = Frame(root,bg="#808080")
btnrow2.pack(expand=True, fill = "both")

btnrow3 = Frame(root, bg="#ffffff") 
btnrow3.pack(expand=True, fill= "both")

btnrow4 = Frame(root, bg="#000000")
btnrow4.pack(expand=True, fill="both")

btnrow5 = Frame(root, bg="#000000")
btnrow5.pack(expand=True, fill="both")


# Fill buttonrow 1 with the 4 buttons

btn1=Button(btnrow1, text ="7", font = ("Verdana", 22), command = btn_7_isclicked, ) #this button is within parent btnrow1, root window is the parent of btnrow1
btn1.pack(side=LEFT, expand=True, fill="both")

btn2=Button(btnrow1, text ="8", font = ("Verdana", 22), command = btn_8_isclicked, ) 
btn2.pack(side=LEFT, expand=True, fill="both")

btn3=Button(btnrow1, text ="9", font = ("Verdana", 22), command = btn_9_isclicked, ) 
btn3.pack(side=LEFT, expand=True, fill="both")

btn4=Button(btnrow1, text ="/", font = ("Verdana", 22), command = btn_division_isclicked, ) 
btn4.pack(side=LEFT, expand=True, fill="both")

# Fill buttonrow 2 with the 4 buttons

btn5=Button(btnrow2, text="4", font =("Verdana", 22), command = btn_4_isclicked, ) #this button is within parent btnrow2, root window is the parent of btnrow2
btn5.pack(side=LEFT, expand=True, fill="both")

btn6=Button(btnrow2, text="5", font =("Verdana", 22), command = btn_5_isclicked, )
btn6.pack(side=LEFT, expand=True, fill="both")


btn7=Button(btnrow2, text="6", font=("Verdana", 22), command = btn_6_isclicked, )
btn7.pack(side=LEFT, expand=True, fill="both")

btn8=Button(btnrow2, text="*", font=("Verdana", 22), command = btn_multiply_isclicked, )
btn8.pack(side=LEFT, expand=True, fill="both")

# Fill buttonrow 3 with the 4 buttons
btn9=Button(btnrow3, text="1", font=("Verdana", 22), command = btn_1_isclicked, ) #this button is within parent btnrow3, root window is the parent of btnrow3
btn9.pack(side=LEFT, expand=True, fill="both")
 #what should happen when the button'1' is clicked

btn10=Button(btnrow3, text="2", font=("Verdana", 22), command = btn_2_isclicked, )
btn10.pack(side=LEFT, expand=True, fill="both")


btn11=Button(btnrow3, text="3", font=("Verdana", 22), command = btn_3_isclicked, )
btn11.pack(side=LEFT,expand=True, fill="both")


btn12=Button(btnrow3, text="-", font=("Verdana", 22), command =btn_minus_isclicked)
btn12.pack(side=LEFT,expand=True, fill="both")

#Fill buttonrow 4 with the 4 buttons 

btn13=Button(btnrow4, text="0", font=("Verdana", 22), command = btn_0_isclicked, )
btn13.pack(side=LEFT, expand=True, fill="both")

btn14=Button(btnrow4, text=".", font=("Verdana", 22), command = btn_decimal_isclicked, )
btn14.pack(side=LEFT, expand=True, fill="both")

btn15=Button(btnrow4, text="+", font=("Verdana", 22), command = btn_plus_clicked,)
btn15.pack(side=LEFT, expand=True, fill="both")

#fill buttonrow 5 with button
btn16=Button(btnrow5, text="Clear", font=("Verdana", 22), command =btn_clear_isclicked,)
btn16.pack(side=LEFT, expand=True, fill="both")

btn17=Button(btnrow5, text="=", font=("Verdana", 22), command =btn_equalto_isclicked, )
btn17.pack(side=LEFT, expand=True, fill="both")

root.mainloop()
