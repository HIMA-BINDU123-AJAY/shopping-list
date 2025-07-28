import tkinter as tk
from tkinter import messagebox
import webbrowser

class ShoppingListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shopping List App")
        self.root.geometry("460x600")
        self.root.config(bg="#f0f8ff")

        self.items = []

        # Title
        title = tk.Label(root, text=" My Shopping List", font=("Arial", 18, "bold"), bg="#f0f8ff", fg="#333")
        title.pack(pady=10)

        # Entry field
        self.entry = tk.Entry(root, font=("Arial", 14), width=30)
        self.entry.pack(pady=5)

        # Add/Delete/Save/Load Buttons
        button_frame = tk.Frame(root, bg="#f0f8ff")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Add Item", command=self.add_item, width=10).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Delete Item", command=self.delete_item, width=10).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Save List", command=self.save_list, width=10).grid(row=1, column=0, pady=5)
        tk.Button(button_frame, text="Load List", command=self.load_list, width=10).grid(row=1, column=1, pady=5)

        # Search Buttons
        search_frame = tk.LabelFrame(root, text="Search Online", font=("Arial", 12, "bold"), bg="#f0f8ff", padx=10, pady=10)
        search_frame.pack(pady=10)

        tk.Button(search_frame, text="Amazon", command=self.search_amazon, width=12, bg="#ff9900", fg="white").grid(row=0, column=0, padx=5, pady=5)
        tk.Button(search_frame, text="Flipkart", command=self.search_flipkart, width=12, bg="#2874f0", fg="white").grid(row=0, column=1, padx=5, pady=5)
        tk.Button(search_frame, text="Meesho", command=self.search_meesho, width=12, bg="#8e44ad", fg="white").grid(row=1, column=0, padx=5, pady=5)
        tk.Button(search_frame, text="Myntra", command=self.search_myntra, width=12, bg="#e91e63", fg="white").grid(row=1, column=1, padx=5, pady=5)

        # Listbox
        self.listbox = tk.Listbox(root, font=("Arial", 14), width=40, height=15, selectbackground="#a1a1a1")
        self.listbox.pack(pady=10)

        self.load_list()

    def add_item(self):
        item = self.entry.get().strip()
        if item:
            self.items.append(item)
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter an item.")

    def delete_item(self):
        try:
            selected = self.listbox.curselection()[0]
            self.items.pop(selected)
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select an item to delete.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for item in self.items:
            self.listbox.insert(tk.END, item)

    def save_list(self):
        with open("shopping_list.txt", "w") as f:
            for item in self.items:
                f.write(item + "\n")
        messagebox.showinfo("Saved", "Shopping list saved successfully.")

    def load_list(self):
        try:
            with open("shopping_list.txt", "r") as f:
                self.items = [line.strip() for line in f.readlines()]
                self.update_listbox()
        except FileNotFoundError:
            pass

    def get_selected_item(self):
        try:
            selected = self.listbox.curselection()[0]
            return self.listbox.get(selected)
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select an item to search.")
            return None

    def search_amazon(self):
        item = self.get_selected_item()
        if item:
            query = item.replace(" ", "+")
            url = f"https://www.amazon.in/s?k={query}"
            webbrowser.open(url)

    def search_flipkart(self):
        item = self.get_selected_item()
        if item:
            query = item.replace(" ", "+")
            url = f"https://www.flipkart.com/search?q={query}"
            webbrowser.open(url)

    def search_meesho(self):
        item = self.get_selected_item()
        if item:
            query = item.replace(" ", "%20")
            url = f"https://www.meesho.com/search?q={query}"
            webbrowser.open(url)

    def search_myntra(self):
        item = self.get_selected_item()
        if item:
            query = item.replace(" ", "%20")
            url = f"https://www.myntra.com/{query}"
            webbrowser.open(url)

if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingListApp(root)
    root.mainloop()
