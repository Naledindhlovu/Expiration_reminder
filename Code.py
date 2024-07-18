# Importing tkinter and login, register libraries
from tkinter import *
from tkinter import messagebox as ms
from tkinter import simpledialog
import tkinter as tk
import sqlite3
#from login import Log
from register import Register
from PIL import ImageTk, Image

import re     
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
 
''' Window Setting Start '''
# Creating Widget
system = tk.Tk()

# Creating size of window
system.attributes('-fullscreen', True)

# Background Colors
system.configure(background='#3B2C35')

# Locking the window size
system.resizable(width=False, height=False)

# Creating Title
system.title('Expiration Reminder System')

# Creating title icon
system.iconbitmap('img/Logo.ico')
''' Window Setting End '''

# Top Frame
# top_frame = Label(system, text='Expiration Reminder',font = ('Times', 25, 'bold'), bg='#87CEEB',relief='groove',padx=500, pady=30,width=400,height=400)
# top_frame.pack(side='top')

# img = Image.open("notify-label.png")
# tkimage = ImageTk.PhotoImage(img)
# img_label = Label(top_frame, image=tkimage).grid()


''' Background Image Start'''
# Sizing Image
canvas = Canvas(system)

# Opening Image
image = ImageTk.PhotoImage(Image.open('img/cheeses.jpg'))

#Positioning Image
canvas.create_image(0,0, anchor=NW, image=image)
canvas.pack(fill=tk.BOTH, expand=True) 
''' Background Image End'''

# Creating Frame
frame = LabelFrame(system,text='', padx=30, pady=40, bg='white', bd='5', relief='groove')
frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)


# Creating login button and positioning it
login = tk.Button(frame, text = "Login", width="10", bd = '3', command=lambda:[Log()], font = ('Times', 12, 'bold'), bg='#87CEEB',relief='groove', justify = 'center', pady='5')
login.pack()

# Label for seperating Buttons
label = Label(frame, bg='white').pack()

# Creating and Positioning Button in Main Frame    
register = tk.Button(frame, text = "Register", width="10", bd = '3',  command=lambda:[Register()], font = ('Times', 12, 'bold'), bg='#4e73df',fg='white', relief='groove', justify = 'center', pady='5')
register.pack()

# Quit Button of main frame 

def Quit():
    response = ms.askokcancel('Exit!', 'Do you really want to exit ?')
    if response == 1:
        system.destroy()
    else:
        pass
    
def Log():
    # Creating a new window
    Login = tk.Tk()
    Login.attributes('-fullscreen', True)
    Login.title('LOGIN')

    # Background Colors
    Login.configure(background='#4e73df')

    # Locking the window size
    Login.resizable(width=False, height=False)

    # Creating title icon
    Login.iconbitmap('img/loginlogo.ico')

    # Top Frame
    top_frame = Label(Login, text='LOGIN',font = ('Times', 25, 'bold'), bg='#4e73df',relief='groove',padx=500, pady=30)
    top_frame.pack(side='top')
    
    # Creating Frame
    frame = LabelFrame(Login, padx=40, pady=30, bg='white')
    frame.place(relx = 0.5, rely = 0.55, anchor = CENTER)
    
    # Creating function for connecting to database and checking username
    def Search(arg = None):
        if username_entry.get() == '': 
            ms.showerror('Oops', 'Enter Username !!')
            
        elif password_entry.get() == '':
            ms.showerror('Oops', 'Enter Password !!')
            
        else:
            global username
            username = username_entry.get()
            global password
            password = password_entry.get()

            # Making connection
            conn = sqlite3.connect('Database.db')

            # Creating cursor
            with conn:
                cursor = conn.cursor()

            # Searching for users
            find_user = ('SELECT * FROM users WHERE Username = ? AND Password = ?')
            cursor.execute(find_user,(username, password))
            results = cursor.fetchall()

            # if user then new window
            if results:
                system.destroy()
                Login.destroy()

                import finalImg
                # result = tk.Tk()
                # result.geometry('500x500')
                # result.title('Thank You !')

                # # Background Colors
                # result.configure()

                # # Locking the window size
                # result.resizable(width=False, height=False)

                # # Showing Result
                #label = tk.Label(result, text = 'Hi '+ username +'\nThank You For Using Our System !!!!',font=('Arial',12, 'bold'),bg='white', fg='green').place(relx = 0.5, rely = 0.5, anchor = CENTER)


                # from noti import notifierpy
            # if user do not exist
            else:
                ms.showerror('Oops','User Not Found !! Check Username and Password Again !!')

    # creating a label for username and password using Label 
    username = tk.Label(frame, text = 'USERNAME',font=('Arial',12, 'bold'),bg='white', fg='#4e73df')
    password = tk.Label(frame, text = 'PASSWORD', font = ('Arial',12,'bold'),bg='white', fg='#4e73df')   

    # creating a entry for username 
    username_entry = tk.Entry(frame, font=('calibre',10,'normal'), justify = 'center', bg='#87CEEB')
    username_entry.bind('<Return>', Search)
    password_entry=tk.Entry(frame, font = ('calibre',10,'normal'), show = '*', justify = 'center', bg='#87CEEB') 
    password_entry.bind('<Return>', Search)
    
    # Button that will call the submit function  
    submit=tk.Button(frame,text = 'Login', command = Search, width="10",bd = '3',  font = ('Times', 12, 'bold'), bg='#581845', fg='white',relief='groove', justify = 'center', pady='5') 

    # Placing the label and entry   
    username.pack()
    username_entry.focus_set()
    username_entry.pack()
    
    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    password.pack() 
    password_entry.pack()

    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    submit.pack()

    # Quit Button
    def destr():
        Login.destroy
        import code

    Quit = tk.Button(Login, text = "BACK", width="10", command=lambda:[Login.destroy(), system.deiconify()], bd = '3',  font = ('Times', 12, 'bold'), bg='black', fg='white',relief='groove', justify = 'center', pady='5')
    Quit.place(anchor ='sw',rely=1,relx=0.775)

# Creating register function
def Register():
    
    # Creating a new window
    Reg = tk.Tk()
    Reg.title('Register in System')
    Reg.attributes('-fullscreen', True)

    # Background Colors
    Reg.configure(background='#87CEEB')

    # Locking the window size
    Reg.resizable(width=False, height=False)

    # Creating title icon
    Reg.iconbitmap('img/reglogo.ico')
    
    # Top Frame
    top_frame = Label(Reg, text='REGISTER',font = ('Times', 25, 'bold'), bg='#4e73df',relief='groove',padx=500, pady=30)
    top_frame.pack(side='top')
    
    # Creating Frame
    frame = LabelFrame(Reg, padx=30, pady=30, bg='white')
    frame.place(relx = 0.5, rely = 0.55, anchor = CENTER)
    
    # Connecting to database with registration form
    def database(arg=None):
      
        # Getting entries
        name = name_entry.get()
        email = email_entry.get()

        # Mobile Number converting to Integer
        mobile = mobile_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        confirm = confirm_entry.get()

        # Validating Entries
        validation = []

        # Adding information to the list
        validation.append(name)
        validation.append(email)
        validation.append(mobile)
        validation.append(username)
        validation.append(password)
        validation.append(confirm)

        # Boolean for condition
        condition = True
        
        # Looping and checking conditions
        for ele in validation:
            if ele == '':
                condition = False
                break

        if condition:
            
            # Checking for password match
            if password != confirm:
                ms.showerror('Oops', 'Password Does Not Match!!!')    
                
            else:
                # Making connection
                conn = sqlite3.connect('Database.db')

                #Creating cursor
                with conn:
                    cursor = conn.cursor()

                # Making table if not exist
                cursor.execute('CREATE TABLE IF NOT EXISTS Users (FullName TEXT NOT NULL, Email TEXT NOT NULL, Mobile TEXT NOT NULL, Username TEXT NOT NULL, Password TEXT NOT NULL)')

                # Inserting Data into Table
                cursor.execute('INSERT INTO Users (FullName, Email, Mobile, Username, Password) VALUES (?,?,?,?,?)', (name, email, mobile, username, password))
                conn.commit()

                # Showing success message
                ms.showinfo('Successful', 'Account Created Successfully!! Now You Can Login To System!!')

                # Closing the window
                Reg.destroy()
            
        else:
            ms.showerror('Oops', 'Please Fill All The Input Fields')
    
    # creating a label for username and password using Label
    name = tk.Label(frame, text = 'Full Name', font=('Arial',12, 'bold'), bg='white', fg='#87CEEB')
    email = tk.Label(frame, text = 'Email', font=('Arial',12, 'bold'), bg='white', fg='#87CEEB')
    mobile = tk.Label(frame, text = 'Mobile No.', font=('Arial',12, 'bold'), bg='white', fg='#87CEEB')
    username = tk.Label(frame, text = 'Username', font=('Arial',12, 'bold'), bg='white', fg='#87CEEB')                    
    password = tk.Label(frame, text = 'Password', font = ('Arial',12,'bold'), bg='white', fg='#87CEEB')
    confirm = tk.Label(frame, text = 'Confirm Password', font=('Arial',12, 'bold'), bg='white', fg='#87CEEB')

    def validate(u_input): # callback function
        return u_input.isdigit()

    def validate1(u_input): # callback function
        return u_input.isalpha()

    def validate2(u_input):
        if(re.search(regex,u_input) and u_input.isalpha):
            print(True)
            submit.config(state='active')  
            return True        
        else:
            print(False)
            #submit.config(state='disabled')  
            return False  

    my_valid = Reg.register(validate)
    my_valid1 = Reg.register(validate1)
    my_valid2 = Reg.register(validate2)
    
    # creating a entry for elements and returning values to the databse function
    name_entry = tk.Entry(frame ,font=('Arial',12,'normal'), bg='#87CEEB', validate='key',validatecommand=(my_valid1,'%S'))
    name_entry.bind("<Return>", database)
    email_entry = tk.Entry(frame,font=('Arial',12,'normal'), bg='#87CEEB', validate='focusout',validatecommand=(my_valid2,'%P'))
    email_entry.bind("<Return>",database)

    mobile_entry = tk.Entry(frame,font=('Arial',12,'normal'), bg='#87CEEB', validate='key',validatecommand=(my_valid,'%S'))

    mobile_entry.bind("<Return>",database)
    username_entry = tk.Entry(frame,font=('Arial',12,'normal'), bg='#87CEEB', validate='key',validatecommand=(my_valid1,'%S'))
    username_entry.bind("<Return>",database)
    password_entry=tk.Entry(frame, font = ('Arial',12,'normal'), show = '*', bg='#87CEEB')
    password_entry.bind("<Return>",database)
    confirm_entry=tk.Entry(frame, font = ('Arial',12,'normal'), show = '*', bg='#87CEEB')
    confirm_entry.bind("<Return>",database)
       
    # Button that will call the submit function  
    submit=tk.Button(frame,text = 'Register', command = database, width="10",bd = '3',  font = ('Times', 12, 'bold'),bg='#581845', fg='white',relief='groove', justify = 'center', pady='5'  ) 
       
    # Placing the label and entry
    name.pack()
    name_entry.focus_set()
    name_entry.pack()
    
    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    email.pack()
    email_entry.pack()

    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    mobile.pack()
    mobile_entry.pack()

    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    username.pack() 
    username_entry.pack()

    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    password.pack() 
    password_entry.pack()

    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    confirm.pack()
    confirm_entry.pack()

    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    submit.pack()

    # Quit Button

    Quit = tk.Button(Reg, text = "BACK", width="10", command=lambda:[Reg.destroy(), system.deiconify()], bd = '3',  font = ('Times', 12, 'bold'), bg='black', fg='white',relief='groove', justify = 'center', pady='5')
    Quit.place(anchor ='sw',rely=1,relx=0.84)

Quit = tk.Button(system, text = "EXIT", width="10", command = Quit, bd = '3',  font = ('Times', 12, 'bold'), bg='red', fg='white',relief='groove', justify = 'center', pady='5')
Quit.place(anchor ='sw',rely=1,relx=0.91)

# Displyaing Widget to Screen
system.mainloop()
