from os import system
from tkinter import *
from tkinter import messagebox as ms
import tkinter as tk
import sqlite3
from PIL import ImageTk, Image

# Creating Input
def Log():
    # Creating a new window
    Login = tk.Tk()
    Login.geometry('700x467')
    Login.title('LOGIN')

    # Background Colors
    Login.configure(background='#4e73df')

    # Locking the window size
    Login.resizable(width=False, height=False)

    # Creating title icon (Make sure the path is correct)
    try:
        Login.iconbitmap('img/loginlogo.ico')
    except Exception as e:
        print(f"Icon not found: {e}")

    # Top Frame
    top_frame = Label(Login, text='LOGIN', font=('Times', 25, 'bold'), bg='#87CEEB', relief='groove', padx=500, pady=30)
    top_frame.pack(side='top')

    # Creating Frame
    frame = LabelFrame(Login, padx=40, pady=30, bg='white')
    frame.place(relx=0.5, rely=0.55, anchor=CENTER)

    # Function for connecting to database and checking username
    def Search(event=None):
        username = username_entry.get()
        password = password_entry.get()

        if username == '':
            ms.showerror('Oops', 'Enter Username !!')
        elif password == '':
            ms.showerror('Oops', 'Enter Password !!')
        else:
            # Making connection
            conn = sqlite3.connect('Database.db')

            # Creating cursor
            with conn:
                cursor = conn.cursor()

            # Searching for users
            find_user = 'SELECT * FROM users WHERE Username = ? AND Password = ?'
            cursor.execute(find_user, (username, password))
            results = cursor.fetchall()

            # If user exists, proceed to the next window
            if results:
                Login.destroy()
                import finalImg  # Assuming this is a module that launches the next window

            # If user does not exist
            else:
                ms.showerror('Oops', 'User Not Found !! Check Username and Password Again !!')

    # Creating labels and entries for username and password
    username_label = tk.Label(frame, text='USERNAME', font=('Arial', 12, 'bold'), bg='white', fg='#4e73df')
    password_label = tk.Label(frame, text='PASSWORD', font=('Arial', 12, 'bold'), bg='white', fg='#4e73df')

    username_entry = tk.Entry(frame, font=('calibre', 10, 'normal'), justify='center', bg='#87CEEB')
    username_entry.bind('<Return>', Search)
    password_entry = tk.Entry(frame, font=('calibre', 10, 'normal'), show='*', justify='center', bg='#87CEEB')
    password_entry.bind('<Return>', Search)

    # Button that will call the submit function
    submit_button = tk.Button(frame, text='Login', command=Search, width="10", bd='3', font=('Times', 12, 'bold'), bg='#581845', fg='white', relief='groove', justify='center', pady='5')

    # Placing the labels and entries
    username_label.pack()
    username_entry.focus_set()
    username_entry.pack()

    # Separator
    Label(frame, bg='white').pack()

    password_label.pack()
    password_entry.pack()

    # Separator
    Label(frame, bg='white').pack()

    submit_button.pack()

    # Quit Button
    def destr():
        Login.destroy()

    Quit = tk.Button(Login, text="BACK", width="10", command=destr, bd='3', font=('Times', 12, 'bold'), bg='black', fg='white', relief='groove', justify='center', pady='5')
    Quit.place(anchor='sw', rely=1, relx=0.775)

    Login.mainloop()

# Call the Log function to run the application
Log()
