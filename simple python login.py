from tkinter import *
import sqlite3

root = Tk()
root.title("Python: Student management system")
width = 400
height = 280
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

#==============================METHODS========================================
def Database():
    global conn, cursor
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")       
    cursor.execute("SELECT * FROM `member` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `member` (username, password) VALUES('admin', 'admin')")
        conn.commit()
    
def Login(event=None):
    Database()


    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            HomeWindow()
            USERNAME.set("")
            PASSWORD.set("")
            lbl_text.config(text="")
        else:
            lbl_text.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")   
    cursor.close()
    conn.close()

def HomeWindow():
    global Home
    root.withdraw()
    Home = Toplevel()
    Home.title("Python: Simple Login Application")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.resizable(0, 0)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    lbl_home = Label(Home, text="Successfully Login!", font=('times new roman', 20)).pack()
    btn_back = Button(Home, text='Back', command=Back).pack(pady=20, fill=X)

def Back():
    Home.destroy()
    root.deiconify()
    
#==============================VARIABLES======================================
USERNAME = StringVar()
PASSWORD = StringVar()

#==============================FRAMES=========================================
Top = Frame(root, bd=2,  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=200)
Form.pack(side=TOP, pady=20)

#==============================LABELS=========================================
lbl_title = Label(Top, text = "Python: Simple Login Application", font=('arial', 15))
lbl_title.pack(fill=X)
lbl_username = Label(Form, text = "Username:", font=('arial', 14), bd=15)
lbl_username.grid(row=0, sticky="e")
lbl_password = Label(Form, text = "Password:", font=('arial', 14), bd=15)
lbl_password.grid(row=1, sticky="e")
lbl_text = Label(Form)
lbl_text.grid(row=2, columnspan=2)

#==============================ENTRY WIDGETS==================================
username = Entry(Form, textvariable=USERNAME, font=(14))
username.grid(row=0, column=1)
password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
password.grid(row=1, column=1)

#==============================BUTTON WIDGETS=================================
btn_login = Button(Form, text="Login", width=45, command=Login)
btn_login.grid(pady=25, row=3, columnspan=2)
btn_login.bind('<Return>', Login)


#While True

#Student management System
rec_fields = ['roll', 'name', 'age', 'email', 'phone']
sms_database = 'student.cvs'
def show_menu():
    print("------------------------------------------")
    print("Welcome to student Management System")
    print("------------------------------------------")
    print("1.Add new student")
    print("2.View student")
    print("3.Search Student")
    print("4.Update students")
    print("5.Delete Students")
    print("6.Quit")
def create_record():
    print("-----------------------------------------")
    print("Add student information")
    print("-----------------------------------------")
    
name = input("Enter your student name: ")
age = input("Enter student age: ")
mark = input("Enter student rate[type read]: ")
name = "Kent"
age = "26"
mark = "test 50 and task 30"
score = "Read"
print("school record" + name + "! They are" + age + "! and" + mark)
print("_______________________________________________________________________________________")

print("in order to get student cass mark add both test and task mark then divide by 2")
num1 = input("enter a number: ")
num2 = input("enter another number: ")
results = float(num1) + float(num2)
print(results/2)
    
print("Enter student marks in the Calculator")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
num1 = float(input("Enter first number: "))
op = input("enter operator: ")
num2 = float(input("Enter second number: "))
    
num1 = input("enter task mark: ")
num2 = input("enter test mark: ")

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
results = float(num1) + float(num2)
print(results/2)
    
if op == "+" :
    print(num1 + num2)
elif op == "-": 
    print(num1 - num2)
elif op== "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("invelid operator")



