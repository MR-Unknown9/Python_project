import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame
from PIL import Image, ImageTk
import sqlite3

DATABASE_FILE = "db/products.db"


class PerfumeShopApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Perfume Shop")
        self.window.geometry("900x600")
        self.window.configure(bg="#fdf5df")  # Dark gray backgroun
        self.window.iconbitmap(
            r"D:\python pr\My git_hub_proj\Python_project\images\icoPerfum.ico"
        )
        self.spinboxes = []
        self.user_name = "Gest1"
        add_product_frame = None  # Initialize globally

        self.create_widgets()
        self.init_db_and_load_products()

    def create_widgets(self):
        title_label = ttk.Label(
            self.window,
            text="Perfume Shop",
            foreground="#E2E2B6",
            font=("ADLaM Display", 35, "bold"),
            background="#fdf5df",
        )
        title_label.pack(side=tk.TOP, pady=10)

        self.main_frame = tk.Frame(self.window)
        self.main_frame.configure(bg="#fdf5df")
        self.main_frame.pack(fill=tk.BOTH, expand=tk.YES, pady=15, padx=15)

        self.button_frame = tk.Frame(self.main_frame, bg="#fdf5df")
        self.button_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)
        self.button_frame.configure(bg="#fdf5df")

        self.toggle_toolbar_button = ttk.Button(
            self.button_frame,
            text="Toggle Toolbar",
            style="info.TButton",
            command=self.toggle_toolbar,
        )
        self.toggle_toolbar_button.pack(side=tk.BOTTOM, pady=5)

        self.toolbar = Toolbar(self.button_frame, self)
        self.toolbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.toolbar.configure(bg="#fdf5df")

        self.scroll_frame = ProductFrame(self.main_frame, self)
        self.scroll_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)

        style = ttk.Style()
        style.configure(
            "warning.TSpinbox",
            darkcolor="#E2E2B6",
            padding=5,
            bordercolor="#E2E2B6",
            arrowcolor="#E2E2B6",
        )
        style.map(
            "warning.TSpinbox",
            darkcolor=[("disabled", "Gold"), ("active", "gold"), ("focus", "gold")],
            arrowcolor=[("disabled", "Gold"), ("active", "gold")],
            fieldbackground=[("disabled", "Gold"), ("active", "gold")],
            bordercolor=[("disabled", "Gold"), ("active", "gold"), ("focus", "gold")],
            foreground=[("disabled", "black"), ("active", "black")],
            background=[("disabled", "white"), ("active", "#f0f8ff")],
        )

        style.configure(
            "info.TButton",
            font="Bold 9",
            background="#5ebec4",
            bordercolor="#5ebec4",
            lightcolor="#5ebec4",
            focuscolor="#5ebec4",
            darkcolor="#5ebec4",
            foreground="black",
        )
        style.map(
            "info.TButton",
            bordercolor=[("disabled", "Gold"), ("active", "gold"), ("focus", "gold")],
            foreground=[("disabled", "black"), ("active", "black")],
            background=[("disabled", "white"), ("active", "#6EACDA")],
        )

    def toggle_toolbar(self):
        if self.toolbar.winfo_ismapped():
            self.toolbar.pack_forget()
        else:
            self.toolbar.pack(side=tk.BOTTOM, fill=tk.X)

    def save_user_choices(self):
        try:
            conn = sqlite3.connect(DATABASE_FILE)
            cursor = conn.cursor()
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS user_selections (user_name TEXT, name TEXT, quantity INTEGER, priceD REAL)"
            )

            for spinbox in self.spinboxes:
                priceD = float(spinbox.product_details["price"])
                user_name = self.user_name
                details = spinbox.product_details
                quantity = int(spinbox.get())

                cursor.execute(
                    "INSERT INTO user_selections (user_name, name, quantity, priceD) VALUES (?, ?, ?, ?)",
                    (user_name, details["name"], quantity, priceD),
                )

            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "User choices saved successfully!")
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to save user choices: {e}")

    def save_product_data(self):
        try:
            conn = sqlite3.connect(DATABASE_FILE)
            cursor = conn.cursor()
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS product_perfum (name TEXT, brand TEXT, price REAL, image_name TEXT)"
            )
            cursor.execute("DELETE FROM product_perfum")
            for spinbox in self.spinboxes:
                details = spinbox.product_details
                cursor.execute(
                    """
                    INSERT INTO product_perfum (name, brand, price, image_name)
                    VALUES (?, ?, ?, ?)
                """,
                    (
                        details["name"],
                        details["brand"],
                        details["price"],
                        details["image_name"],
                    ),
                )
            conn.commit()
            conn.close()
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to save product data: {e}")

    def load_product_data(self):
        try:
            conn = sqlite3.connect(DATABASE_FILE)
            cursor = conn.cursor()
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS product_perfum (name TEXT, brand TEXT, price REAL, image_name TEXT)"
            )
            cursor.execute("SELECT name, brand, price, image_name FROM product_perfum")
            data = cursor.fetchall()
            conn.close()
            return [
                {"name": row[0], "brand": row[1], "price": row[2], "image_name": row[3]}
                for row in data
            ]
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to load product data: {e}")
            return []

    def init_db_and_load_products(self):
        products = self.load_product_data()
        self.scroll_frame.clear_products()
        self.scroll_frame.load_existing_products(products)


class Toolbar(tk.Frame):
    def __init__(self, window, app):
        super().__init__(window)
        self.app = app
        self.create_widgets()

    def create_widgets(self):
        buttons = [
            ("Main Page", "info.TButton", self.go_to_Main_Page),
            ("Perfume Shop", "info.TButton", self.go_to_perfume_shop),
            ("Coffee Shop", "info.TButton", self.go_to_coffee_shop),
            ("Clothes Shop", "info.TButton", self.go_to_clothes_shop),
            ("Cart Page", "info.TButton"),
            ("Add Product", "info.TButton", self.open_add_product_frame),
            ("Delete Product", "info.TButton", self.open_delete_product_frame),
            ("Submit Data", "info.TButton", self.app.save_user_choices),
        ]

        for text, style, *command in buttons:
            button = ttk.Button(
                self, text=text, style=style, command=command[0] if command else None
            )
            button.pack(side=tk.LEFT, padx=5, pady=5)

    # In Clothes_shop.py
    def go_to_perfume_shop(self):
        from Perfume_shop import PerfumeShopApp

        for widget in self.app.window.winfo_children():
            widget.destroy()
        PerfumeShopApp(self.app.window)

    # In Coffe_shop.py
    def go_to_clothes_shop(self):
        from Clothes_shop import ClothesShopApp

        for widget in self.app.window.winfo_children():
            widget.destroy()
        ClothesShopApp(self.app.window)

        # In Clothes_shop.py

    def go_to_coffee_shop(self):
        from Coffe_shop import CofeeShopApp

        for widget in self.app.window.winfo_children():
            widget.destroy()
        CofeeShopApp(self.app.window)

    def go_to_Main_Page(self):
        from Main_Gui import MainPage

        for widget in self.app.window.winfo_children():
            widget.destroy()
        MainPage(self.app.window)

    def open_add_product_frame(self):
        ProductDialog(self.app, mode="add")

    def open_delete_product_frame(self):
        ProductDialog(self.app, mode="delete")


class ProductFrame(ScrolledFrame):
    def __init__(self, window, app):
        super().__init__(window, autohide=True, bootstyle="dark")
        self.app = app
        self.scroll_frame = tk.Frame(self)
        self.scroll_frame.pack(fill=tk.BOTH, expand=tk.YES)

        self.left_frame = tk.Frame(self.scroll_frame)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)

        self.right_frame = tk.Frame(self.scroll_frame)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=tk.YES)

    def clear_products(self):
        for widget in self.left_frame.winfo_children():
            widget.destroy()
        for widget in self.right_frame.winfo_children():
            widget.destroy()
        self.app.spinboxes.clear()

    def load_existing_products(self, products):
        for product in products:
            self.add_product(product)

    def add_product(self, product):
        name = product["name"]
        brand = product["brand"]
        price = product["price"]
        image_name = product["image_name"]

        try:
            img = Image.open(image_name).resize((200, 200))
            tk_img = ImageTk.PhotoImage(img)
        except Exception as e:
            messagebox.showerror("Image Error", f"Failed to load image: {e}")
            return

        pair_frame = tk.Frame(
            self.left_frame if len(self.app.spinboxes) % 2 == 0 else self.right_frame
        )
        pair_frame.pack(padx=5, pady=5, fill=tk.BOTH, expand=tk.YES)

        img_label = ttk.Label(pair_frame, image=tk_img)
        img_label.image = tk_img
        img_label.pack(pady=(0, 5))

        details = f"Name: {name}\nBrand: {brand}\nPrice: {price}$"
        details_label = ttk.Label(
            pair_frame,
            text=details,
            anchor=tk.W,
            justify=tk.LEFT,
            font=("Arial", 9, "bold"),
        )
        details_label.pack(pady=(0, 5))

        spinbox = ttk.Spinbox(
            pair_frame, from_=1, to=100, style="warning.TSpinbox", width=10
        )
        spinbox.pack(pady=(0, 5))
        self.app.spinboxes.append(spinbox)

        spinbox.product_details = product


class ProductDialog(tk.Toplevel):
    def __init__(self, app, mode="add"):
        super().__init__(app.window)
        self.app = app
        self.mode = mode
        self.title(f"{mode.capitalize()} Product")
        self.geometry("350x400")

        if mode == "add":
            self.create_add_product_widgets()
        elif mode == "delete":
            self.create_delete_product_widgets()

    def create_add_product_widgets(self):
        ttk.Label(self, text="Product Name:").pack(pady=5)
        self.product_name_entry = ttk.Entry(self)
        self.product_name_entry.pack(pady=5)

        ttk.Label(self, text="Brand:").pack(pady=5)
        self.product_brand_entry = ttk.Entry(self)
        self.product_brand_entry.pack(pady=5)

        ttk.Label(self, text="Price:").pack(pady=5)
        self.product_price_entry = ttk.Entry(self)
        self.product_price_entry.pack(pady=5)

        ttk.Label(self, text="Image Name:").pack(pady=5)
        self.image_name_entry = ttk.Entry(self)
        self.image_name_entry.pack(pady=5)

        ttk.Button(self, text="Add Product", command=self.add_product).pack(pady=10)

    def add_product(self):
        product = {
            "name": self.product_name_entry.get(),
            "brand": self.product_brand_entry.get(),
            "price": self.product_price_entry.get(),
            "image_name": self.image_name_entry.get(),
        }
        self.app.scroll_frame.add_product(product)
        self.app.save_product_data()  # Save the new product to the database
        self.destroy()

    def create_delete_product_widgets(self):
        ttk.Label(self, text="Select Product to Delete:").pack(pady=5)
        self.product_listbox = tk.Listbox(self)
        self.product_listbox.pack(fill=tk.BOTH, expand=tk.YES, pady=5)

        products = self.app.load_product_data()
        for product in products:
            self.product_listbox.insert(tk.END, product["name"])

        ttk.Button(self, text="Delete Product", command=self.delete_product).pack(
            pady=10
        )

    def delete_product(self):
        selected_product = self.product_listbox.get(tk.ACTIVE)
        if selected_product:
            products = self.app.load_product_data()
            updated_products = [p for p in products if p["name"] != selected_product]
            self.app.scroll_frame.clear_products()
            self.app.scroll_frame.load_existing_products(updated_products)
            self.app.save_product_data()
            self.destroy()


if __name__ == "__main__":
    root = ttk.Window()
    app = PerfumeShopApp(root)
    root.mainloop()
