from tkinter import *
from tkinter import messagebox as ms
import tkinter as tk
import sqlite3
from PIL import ImageTk, Image

# Creating register function
def Register():
    
    # Creating a new window
    Reg = tk.Tk()
    Reg.title('Register in System')
    Reg.geometry('700x700')

    # Background Colors
    Reg.configure(background='#87CEEB')

    # Locking the window size
    Reg.resizable(width=False, height=False)

    # Creating title icon (Ensure the path is correct)
    try:
        Reg.iconbitmap('img/reglogo.ico')
    except Exception as e:
        print(f"Icon not found: {e}")
    
    # Top Frame
    top_frame = Label(Reg, text='REGISTER',font=('Times', 25, 'bold'), bg='#4e73df', relief='groove', padx=500, pady=30)
    top_frame.pack(side='top')
    
    # Creating Frame
    frame = LabelFrame(Reg, padx=30, pady=30, bg='white')
    frame.place(relx=0.5, rely=0.55, anchor=CENTER)
    
    # Connecting to database with registration form
    def database(arg=None):
      
        # Getting entries
        name = name_entry.get()
        email = email_entry.get()

        # Mobile Number converting to Integer
        mobile = mobile_entry.get()
        try:
            mobile = int(mobile)
        except ValueError:
            ms.showerror('Oops', 'Please Enter a Valid Phone Number !!!')
            return

        username = username_entry.get()
        password = password_entry.get()
        confirm = confirm_entry.get()

        # Validating Entries
        validation = [name, email, mobile, username, password, confirm]

        # Check if any entry is empty
        if '' in validation:
            ms.showerror('Oops', 'Please Fill All The Input Fields')
            return

        # Checking for password match
        if password != confirm:
            ms.showerror('Oops', 'Password Does Not Match!!!')
            return

        # Making connection
        conn = sqlite3.connect('Database.db')

        # Creating cursor
        with conn:
            cursor = conn.cursor()

        # Making table if not exists
        cursor.execute('CREATE TABLE IF NOT EXISTS Users (FullName TEXT NOT NULL, Email TEXT NOT NULL, Mobile TEXT NOT NULL, Username TEXT NOT NULL, Password TEXT NOT NULL)')

        # Inserting Data into Table
        cursor.execute('INSERT INTO Users (FullName, Email, Mobile, Username, Password) VALUES (?,?,?,?,?)', (name, email, mobile, username, password))
        conn.commit()

        # Showing success message
        ms.showinfo('Successful', 'Account Created Successfully!! Now You Can Login To System!!')

        # Closing the window
        Reg.destroy()
    
    # Creating labels and entries for the registration form
    labels = {
        'Full Name': 'name',
        'Email': 'email',
        'Mobile No.': 'mobile',
        'Username': 'username',
        'Password': 'password',
        'Confirm Password': 'confirm',
    }
    
    entries = {}
    
    for text, var in labels.items():
        label = tk.Label(frame, text=text, font=('Arial', 12, 'bold'), bg='white', fg='#87CEEB')
        label.pack()
        entry = tk.Entry(frame, font=('Arial', 12, 'normal'), bg='#87CEEB', show='*' if 'Password' in text else None)
        entry.bind("<Return>", database)
        entry.pack()
        entries[var] = entry
        label = Label(frame, bg='white').pack()  # Separator

    # Unpack entries for easier access
    name_entry = entries['name']
    email_entry = entries['email']
    mobile_entry = entries['mobile']
    username_entry = entries['username']
    password_entry = entries['password']
    confirm_entry = entries['confirm']

    name_entry.focus_set()
    
    # Submit Button
    submit = tk.Button(frame, text='Register', command=database, width="10", bd='3', font=('Times', 12, 'bold'), bg='#581845', fg='white', relief='groove', justify='center', pady='5')
    submit.pack()

    # Quit Button
    Quit = tk.Button(Reg, text="BACK", width="10", command=Reg.destroy, bd='3', font=('Times', 12, 'bold'), bg='black', fg='white', relief='groove', justify='center', pady='5')
    Quit.place(anchor='sw', rely=1, relx=0.84)

    Reg.mainloop()

# Call the Register function to run the application
Register()
