import tkinter as tk
import ttkbootstrap as ttk

window = ttk.Window(themename="cyborg")
window.title("Login")
window.geometry("500x600")

# colamn configeration
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

# row configeration
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)

# "log in" label
login_text = ttk.Label(window, text="Log in", font="roboto 25 bold")
login_text.pack(pady=50)

# Username field
username_frame = ttk.Frame(window)
username = ttk.Label(username_frame, text="Username", font="roboto 18 bold")
username_input = ttk.Entry(username_frame)
username.pack(padx=20, side="left")
username_input.pack()
username_frame.pack(pady=20)

# Password field
password_frame = ttk.Frame(window)
password = ttk.Label(password_frame, text="Password", font="roboto 18 bold")
password_input = ttk.Entry(password_frame, show="*")
password.pack(padx=20, side="left")
password_input.pack()
password_frame.pack(pady=20)

# log in button field
login_button = ttk.Button(window, text="Login", width=20)
login_button.pack(pady=20)

# sign up field
signup_frame = ttk.Frame(window)
signup_text = ttk.Label(signup_frame, text="Don't have an account?")
signup_button = ttk.Button(signup_frame, text="Sign up")
signup_text.pack(side="left", padx=20)
signup_button.pack()
signup_frame.pack()

window.mainloop()
