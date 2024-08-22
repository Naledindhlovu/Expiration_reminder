# Expiration_reminder

-Expiration Reminder Application
This README provides an overview of the "Expiration Reminder" application, a simple tool that allows users to manage and monitor products and their expiration dates using a GUI interface built with Tkinter and a SQLite database for data storage.

-Features
Display Products: Displays a list of products with their barcode, name, expiration date, and associated image.

Delete Products: Users can select and delete a product from the database.

Add Products: Placeholder for adding new products to the database (to be implemented).

-Prerequisites

Before running the application, ensure you have the following installed:

Python 3.x

Tkinter (usually included with Python)

SQLite3 (included with Python)

Files

main.py: Main application script.

Image_data.db: SQLite database where product information is stored.

noti.py: External script for notification handling (not fully integrated in this example).

-Code Overview

1. Importing Libraries
python
Copy code
import sqlite3
from tkinter import *
from tkinter import ttk
sqlite3: Used to interact with the SQLite database.
tkinter: Provides the GUI components.
ttk: Provides themed widgets for the Tkinter GUI.

2. Initial Setup
   
Initializes the main application window with a specified title and size.

Creates a Treeview widget to display the product list.

4. Utility Functions
   
-Reverse Tuple Function:

Reverses the order of tuples (used for displaying data).

-Future Improvements

Add Functionality: Implement the add_data() function to allow adding new products.

Notifications: Integrate the noti.py script to notify users of upcoming expiration dates.

UI Enhancements: Improve the user interface for better usability and appearance.

-License

This project is open-source and free to use under the MIT License.

-Author 
Naledi Ndhlovu







   
