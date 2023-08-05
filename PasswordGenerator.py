import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip 
from PIL import Image, ImageTk

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Please select at least one character type.")
        return ""

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to update the password label
def update_password_label():
    length = int(length_entry.get())
    use_uppercase = uppercase_var.get()
    use_lowercase = lowercase_var.get()
    use_digits = digits_var.get()
    use_special_chars = special_chars_var.get()

    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)
    generated_password.set(password)

def on_generate_click():
    try:
        length = int(length_entry.get())
        use_uppercase = uppercase_var.get()
        use_lowercase = lowercase_var.get()
        use_digits = digits_var.get()
        use_special_chars = special_chars_var.get()

        if length <= 0:
            messagebox.showerror("Error", "Password length should be a positive integer.")
            return

        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)
        if password:
            password_label.config(text="Generated Password: " + password)
            generated_password.set(password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive integer for password length.")

def on_copy_password_click():
    password_to_copy = generated_password.get()
    if password_to_copy:
        pyperclip.copy(password_to_copy)
        messagebox.showinfo("Copy Password", "Password copied to clipboard.")

def on_reset_click():
    length_entry.delete(0, tk.END)
    uppercase_var.set(0)
    lowercase_var.set(0)
    digits_var.set(0)
    special_chars_var.set(0)
    password_label.config(text="")
    generated_password.set("")

# Create the main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x550")
window.configure(bg="light green")

# Load the background image
background_image = Image.open("pg4.jpg")  # Replace "password_generator.jpg" with the actual image file path
background_photo = ImageTk.PhotoImage(background_image)

# Create a Label widget to hold the background image
background_label = tk.Label(window, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create widgets
username_label = tk.Label(window, text="Enter Username", bg='orange', fg='black', font=("Arial", 16, "bold"))
username_label.pack(pady=10)

username_entry = tk.Text(window, width=30, height=1, font=("Arial", 12), wrap='word')
username_entry.pack(pady=5)

length_label = tk.Label(window, text="Enter Password Length",bg='orange',fg='black',font=("Arial", 16, "bold"))
length_label.pack(pady=10)

# Entry widget for password length (made global)
length_entry = tk.Entry(window, width=30)
length_entry.pack(pady=5)

# Function to handle the password generation
def on_generate_click():
    update_password_label()

uppercase_var = tk.IntVar()
uppercase_checkbutton = tk.Checkbutton(window, text="Uppercase Letters", variable=uppercase_var,bg='red',fg='black',font=("Arial", 13, "bold"))
uppercase_checkbutton.pack(pady=5)

lowercase_var = tk.IntVar()
lowercase_checkbutton = tk.Checkbutton(window, text="Lowercase Letters", variable=lowercase_var,bg='red',fg='black',font=("Arial", 13, "bold"))
lowercase_checkbutton.pack(pady=5)

digits_var = tk.IntVar()
digits_checkbutton = tk.Checkbutton(window, text="Digits", variable=digits_var,bg='red',fg='black',font=("Arial", 13, "bold"))
digits_checkbutton.pack(padx=5, pady=5)

special_chars_var = tk.IntVar()
special_chars_checkbutton = tk.Checkbutton(window, text="Special Characters", variable=special_chars_var,bg='red',fg='black',font=("Arial", 13, "bold"))
special_chars_checkbutton.pack(pady=5)

generate_button = tk.Button(window, text="Generate Password", command=on_generate_click,bg='orange',fg='black',font=("Arial", 14, "bold"))
generate_button.pack(pady=10)

password_label = tk.Label(window, text="")
password_label.pack(pady=5)

# Generated Password Variable
generated_password = tk.StringVar()
generated_password.set("")
generated_password_label = tk.Label(window, textvariable=generated_password, font=("Arial", 20, "bold"),bg='green')
generated_password_label.pack(pady=5)

copy_password_button = tk.Button(window, text="Copy Password", command=on_copy_password_click,bg='yellow',fg='black',font=("Arial", 14, "bold"))
copy_password_button.pack(pady=5)

reset_button = tk.Button(window, text="Reset", command=on_reset_click,bg='red',fg='black',font=("Arial", 14, "bold"))
reset_button.pack(pady=5)

# Start the main loop
window.mainloop()