import tkinter as tk
import ttkbootstrap as ttk
import sqlite3


class Checkout:
    def __init__(self):
        self.root = ttk.Window(themename="cyborg")
        self.root.title("Checkout")

        # Create a treeview to display item details
        self.tree = ttk.Treeview(self.root, columns=("id", "Name", "Quantity", "Price"))
        self.tree.heading("#1", text="id", anchor="nw")
        self.tree.heading("#2", text="Name", anchor="nw")
        self.tree.heading("#3", text="Quantity", anchor="nw")
        self.tree.heading("#4", text="Price", anchor="nw")
        self.tree.pack(padx=10, pady=10)

        # Fetch data from the database and populate the treeview
        self.load_items()

        # Display total price
        self.total_label = tk.Label(self.root, text="Total Price:", font="roboto 18")
        self.total_label.pack(side="right", padx=50)  # Align to the right

        # Add a Delete button
        self.delete_button = tk.Button(
            self.root, text="Delete", command=self.delete_item, height=2, width=10
        )
        self.delete_button.pack(side="left", padx=10, pady=10)

    def load_items(self):
        connection = sqlite3.connect("db/inventory.db")
        cursor = connection.cursor()
        cursor.execute("SELECT id, name, quantity, price FROM items")
        data = cursor.fetchall()
        connection.close()

        # Populate the treeview with item details
        for item in data:
            self.tree.insert("", "end", values=item)

    def delete_item(self):
        selected_item = self.tree.item(self.tree.selection())["values"]
        if selected_item:
            item_id = selected_item[0]
            print(f"Deleting item with ID {item_id}")
            try:
                connection = sqlite3.connect("db/inventory.db")
                cursor = connection.cursor()
                cursor.execute("DELETE FROM items WHERE id = ?", (item_id,))
                connection.commit()
                connection.close()
                print("Item deleted successfully")
            except sqlite3.Error as e:
                print(f"Error deleting item: {e}")
            self.tree.delete(self.tree.selection())

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = Checkout()
    app.run()
