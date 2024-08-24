import tkinter as tk
import ttkbootstrap as ttk
import sqlite3
from tkinter import messagebox

DATABASE_FILE = "products.db"

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("500x600")

        self.conn = sqlite3.connect(DATABASE_FILE)
        self.cursor = self.conn.cursor()
        
        self.create_tables()
        
        self.setup_ui()

    def create_tables(self):
        # Create tables if they don't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS login_T (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Sign_Up (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')

        self.conn.commit()

    def setup_ui(self):
        self.login_frame = ttk.Frame(self.root)
        self.signup_frame = ttk.Frame(self.root)

        self.setup_login_frame()
        self.setup_signup_frame()

        self.login_frame.pack(pady=50)

    def setup_login_frame(self):
        login_text = ttk.Label(self.login_frame, text="Log in", font="roboto 25 bold")
        login_text.pack(pady=50)

        username_frame = ttk.Frame(self.login_frame)
        username_label = ttk.Label(username_frame, text="Username", font="roboto 18 bold")
        self.username_input = ttk.Entry(username_frame)
        username_label.pack(padx=20, side="left")
        self.username_input.pack()
        username_frame.pack(pady=20)

        password_frame = ttk.Frame(self.login_frame)
        password_label = ttk.Label(password_frame, text="Password", font="roboto 18 bold")
        self.password_input = ttk.Entry(password_frame, show="*")
        password_label.pack(padx=20, side="left")
        self.password_input.pack()
        password_frame.pack(pady=20)

        login_button = ttk.Button(self.login_frame, text="Login", width=20, command=self.handle_login)
        login_button.pack(pady=20)

        signup_prompt_frame = ttk.Frame(self.login_frame)
        signup_text = ttk.Label(signup_prompt_frame, text="Don't have an account?")
        signup_button = ttk.Button(signup_prompt_frame, text="Sign up", command=self.open_signup)
        signup_text.pack(side="left", padx=20)
        signup_button.pack()
        signup_prompt_frame.pack(pady=10)

    def setup_signup_frame(self):
        signup_title = ttk.Label(self.signup_frame, text="Sign Up", font="roboto 25 bold")
        signup_title.pack(pady=20)

        name_frame = ttk.Frame(self.signup_frame)
        name_label = ttk.Label(name_frame, text="Name", font="roboto 18 bold")
        self.name_input = ttk.Entry(name_frame)
        name_label.pack(padx=20, side="left")
        self.name_input.pack()
        name_frame.pack(pady=20)

        email_frame = ttk.Frame(self.signup_frame)
        email_label = ttk.Label(email_frame, text="Email", font="roboto 18 bold")
        self.email_input = ttk.Entry(email_frame)
        email_label.pack(padx=20, side="left")
        self.email_input.pack()
        email_frame.pack(pady=20)

        password_frame = ttk.Frame(self.signup_frame)
        signup_password_label = ttk.Label(password_frame, text="Password", font="roboto 18 bold")
        self.signup_password_input = ttk.Entry(password_frame, show="*")
        signup_password_label.pack(padx=20, side="left")
        self.signup_password_input.pack()
        password_frame.pack(pady=20)

        signup_button = ttk.Button(self.signup_frame, text="Sign Up", width=20, command=self.handle_signup)
        signup_button.pack(pady=20)

        back_to_login_button = ttk.Button(self.signup_frame, text="Back to Login", command=self.return_to_login)
        back_to_login_button.pack(pady=10)

    def open_signup(self):
        self.login_frame.pack_forget()
        self.signup_frame.pack(pady=50)

    def return_to_login(self):
        self.signup_frame.pack_forget()
        self.login_frame.pack(pady=50)

    def handle_login(self):
        username_data = self.username_input.get()
        password_data = self.password_input.get()
        
        self.cursor.execute('''
            SELECT * FROM Sign_Up WHERE username=? AND password=?
        ''', (username_data, password_data))
        result = self.cursor.fetchone()

        if result:
            messagebox.showinfo("Success", "Login successful!")
            self.go_to_main_page()
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    def handle_signup(self):
        name_data = self.name_input.get()
        email_data = self.email_input.get()
        password_data = self.signup_password_input.get()

        if not name_data or not email_data or not password_data:
            messagebox.showerror("Error", "All fields are required.")
            return

        self.cursor.execute('''
            SELECT * FROM Sign_Up WHERE username=?
        ''', (name_data,))
        if self.cursor.fetchone():
            messagebox.showerror("Error", "Username already exists.")
            return

        self.cursor.execute('''
            INSERT INTO Sign_Up (username, email, password)
            VALUES (?, ?, ?)
        ''', (name_data, email_data, password_data))

        self.cursor.execute('''
            INSERT INTO login_T (username, password)
            VALUES (?, ?)
        ''', (name_data, password_data))

        self.conn.commit()
        messagebox.showinfo("Success", "Sign-up successful!")
        
        self.signup_frame.pack_forget()
        self.login_frame.pack(pady=50)

    def go_to_main_page(self):
        from Main_Gui import MainPage
        for widget in self.root.winfo_children():
            widget.destroy()
        MainPage(self.root)

    def __del__(self):
        self.conn.close()

if __name__ == "__main__":
    root = ttk.Window()
    app = LoginApp(root)
    root.mainloop()
