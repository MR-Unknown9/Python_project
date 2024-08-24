import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk
from PIL import Image, ImageTk
from Perfume_shop import PerfumeShopApp
from Coffe_shop import CofeeShopApp
from Clothes_shop import ClothesShopApp


class MainPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry("900x600")
        self.window.configure(bg="#fdf5df")  # Dark gray backgroun
        self.window.iconbitmap(
            r"D:\python pr\My git_hub_proj\Python_project\images\icoPerfum.ico"
        )
        self.create_styles()
        self.create_widgets()

    def create_styles(self):
        style = ttk.Style()
        style.configure(
            "info.TLabelframe",
            lightcolor="#fdf5df",
            darkcolor="#fdf5df",
            foreground="#fdf5df",
            bordercolor="#fdf5df",
            background="#fdf5df",
        )
        style.configure(
            "info.TButton",
            background="#6EACDA",
            bordercolor="#6EACDA",
            lightcolor="#6EACDA",
            focuscolor="#6EACDA",
            darkcolor="#6EACDA",
        )
        style.configure("info.TRadiobutton", foreground="black", font="Bold")
        style.configure("success.TRadiobutton", foreground="white", font="Bold")
        style.map(
            "info.TButton",
            foreground=[("disabled", "black"), ("active", "black")],
            background=[("disabled", "white"), ("active", "#f0f8ff")],
        )

    def create_widgets(self):
        # Frame for buttons
        Info_frame = ttk.Labelframe(
            self.window, style="info.TLabelframe", text="Nave Bar", width=200
        )
        Info_frame.place(x=350, y=0)

        self.create_buttons(Info_frame)
        self.create_labels()
        self.create_images()

    def create_buttons(self, frame):
        buttons = [
            ("Main Page", "info.TButton"),
            ("Perfume Shop", "info.TButton", self.go_to_perfume_shop),
            ("Coffee Shop", "info.TButton", self.go_to_coffee_shop),
            ("Clothes Shop", "info.TButton", self.go_to_clothes_shop),
            ("Cart Page", "info.TButton"),
        ]
        for i, (text, style, *command) in enumerate(buttons):
            button = ttk.Button(
                frame, text=text, style=style, command=command[0] if command else None
            )
            button.grid(row=0, column=i, padx=10, pady=5)

        for i in range(len(buttons)):
            frame.columnconfigure(i, weight=1)

    def go_to_perfume_shop(self):
        from Perfume_shop import PerfumeShopApp

        for widget in self.window.winfo_children():
            widget.destroy()
        PerfumeShopApp(self.window)

    def go_to_clothes_shop(self):
        from Clothes_shop import ClothesShopApp

        for widget in self.window.winfo_children():
            widget.destroy()
        ClothesShopApp(self.window)

    def go_to_coffee_shop(self):
        from Coffe_shop import CofeeShopApp

        for widget in self.window.winfo_children():
            widget.destroy()
        CofeeShopApp(self.window)

    def create_labels(self):
        ttk.Label(
            self.window,
            text="Online Shopping",
            font="roboto 35 bold",
            foreground="#6EACDA",
            background="#fdf5df",
        ).place(x=500, y=100)
        ttk.Label(
            self.window,
            text="""Welcome to our online store!
We are delighted to have you join our family.
If you have any questions or need assistance,
our support team is here to help.
Happy shopping!""",
            font="roboto 10 bold",
            foreground="#E2E2B6",
            background="#fdf5df",
        ).place(x=500, y=170)

    def create_images(self):
        # Create a canvas to hold the image with a background color
        canvas1 = tk.Canvas(
            self.window, width=60, height=60, bg="#fdf5df", bd=0, highlightthickness=0
        )
        canvas1.place(x=20, y=5)

        # Draw the background color
        canvas1.create_rectangle(0, 0, 60, 60, fill="#fdf5df", outline="#fdf5df")

        # Load and resize the image
        image1 = Image.open("images/2222.png").resize((60, 60))
        image_tk1 = ImageTk.PhotoImage(image1)

        # Place the image on the canvas
        canvas1.create_image(0, 0, anchor="nw", image=image_tk1)
        self.window.image_tk1 = (
            image_tk1  # Keep a reference to avoid garbage collection
        )

        # Repeat for additional images
        canvas2 = tk.Canvas(
            self.window, width=340, height=340, bg="#fdf5df", bd=0, highlightthickness=0
        )
        canvas2.place(x=80, y=150)
        canvas2.create_rectangle(0, 0, 340, 340, fill="#fdf5df", outline="#fdf5df")
        image2 = Image.open("images/on20.png").resize((340, 340))
        image_tk2 = ImageTk.PhotoImage(image2)
        canvas2.create_image(0, 0, anchor="nw", image=image_tk2)
        self.window.image_tk2 = image_tk2

        canvas3 = tk.Canvas(
            self.window, width=300, height=300, bg="#fdf5df", bd=0, highlightthickness=0
        )
        canvas3.place(x=520, y=280)
        canvas3.create_rectangle(0, 0, 300, 300, fill="#fdf5df", outline="#fdf5df")
        image3 = Image.open("images/11111.png").resize((300, 300))
        image_tk3 = ImageTk.PhotoImage(image3)
        canvas3.create_image(0, 0, anchor="nw", image=image_tk3)
        self.window.image_tk3 = image_tk3


if __name__ == "__main__":
    window = ttk.Window()
    app = MainPage(window)
    window.mainloop()
