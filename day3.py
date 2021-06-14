#importing library
from tkinter import *
from tkinter import ttk, Tk

window: Tk = Tk()
#Declaring Window Title
window.title("Registration Form")
#Declaring Window size
window.geometry('300x300')
#Declaring Window Color
window.configure(background = "lavender")
Firstname = Label(window ,text = "First Name").grid(row = 0,column = 0)
LastName = Label(window ,text = "Last Name").grid(row = 1,column = 0)
Email = Label(window ,text = "Email Id").grid(row = 2,column = 0)
Mobile = Label(window ,text = "Contact Number 1").grid(row = 3,column = 0)
AlternateMobile = Label(window ,text = "Contact Number 2").grid(row = 4,column = 0)
Country = Label(window ,text = "Country").grid(row = 5,column = 0)
n=StringVar()
countrylist = OptionMenu(window, n, "India","South Korea", "Switzerland", "Japan", "China", "Canada","Other Asian", "North America", "South America").grid(row = 5,column=1)
n.set('select your country')
Gender = Label(window ,text = "Gender").grid(row = 6,column = 0)
var = IntVar()
Radiobutton(window, text="Male", variable=var, value=1).grid(row = 6,column=1)
Radiobutton(window, text="Female", variable=var, value=2).grid(row = 6,column=2)
DateofBirth = Label(window ,text = "Date of Birth (dd/mm/yy)").grid(row = 7,column = 0)


Firstname1 = Entry(window).grid(row = 0,column = 1)
Lastname1 = Entry(window).grid(row = 1,column = 1)
Email1 = Entry(window).grid(row = 2,column = 1)
Mobile1 = Entry(window).grid(row = 3,column = 1)
AlternateMobile1 = Entry(window).grid(row = 4,column = 1)
DateofBirth1 = Entry(window).grid(row = 7,column = 1)

#function declaration
def clicked():
 res = "Welcome to" + txt.get()
 lbl.configure(text=res)
btn = ttk.Button(window ,text="Submit" , ).grid(row=8,column=1)
window.mainloop()
