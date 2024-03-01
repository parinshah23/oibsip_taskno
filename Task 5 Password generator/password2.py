import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string
import pyperclip
import csv

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_label = ttk.Label(root, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.length_entry = ttk.Entry(root)
        self.length_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        self.length_entry.insert(0, "0")  # Default password length

        self.complexity_label = ttk.Label(root, text="Password Complexity:")
        self.complexity_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.complexity_combo = ttk.Combobox(root, values=["Low", "Medium", "High"])
        self.complexity_combo.current(1)  # Default complexity: Medium
        self.complexity_combo.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.generate_button = ttk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=2, columnspan=2, padx=10, pady=10)

        self.password_label = ttk.Label(root, text="Generated Password:")
        self.password_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.password_entry = ttk.Entry(root, show="*")
        self.password_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        self.copy_button = ttk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.grid(row=4, columnspan=2, padx=10, pady=10)

        self.save_button = ttk.Button(root, text="Save Password", command=self.save_password)
        self.save_button.grid(row=5, columnspan=2, padx=10, pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            complexity = self.complexity_combo.get()
            if complexity == "Low":
                use_letters = True
                use_numbers = False
                use_symbols = False
            elif complexity == "Medium":
                use_letters = True
                use_numbers = True
                use_symbols = False
            else:  # High complexity
                use_letters = True
                use_numbers = True
                use_symbols = True

            password = self.generate_random_password(length, use_letters, use_numbers, use_symbols)
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, password)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for password length.")

    def generate_random_password(self, length, use_letters=True, use_numbers=True, use_symbols=True):
        characters = ''
        if use_letters:
            characters += string.ascii_letters
        if use_numbers:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "No character types selected.")
            return None

        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def copy_to_clipboard(self):
        password = self.password_entry.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Success", "Password copied to clipboard.")
        else:
            messagebox.showerror("Error", "No password generated yet.")

    def save_password(self):
        password = self.password_entry.get()
        if password:
            try:
                with open("passwords.csv", "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([password])
                messagebox.showinfo("Success", "Password saved to passwords.csv.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showerror("Error", "No password generated yet.")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
