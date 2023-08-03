import tkinter as tk
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def cos():
    try:
        expression = entry_num1.get()
        result = math.cos(eval(expression))
        entry_num1.delete(0, tk.END)
        entry_num1.insert(tk.END, str(result))
    except Exception:
        entry_num1.delete(0, tk.END)
        entry_num1.insert(tk.END, "Error")

def sin():
    try:
        expression = entry_num1.get()
        result = math.sin(eval(expression))
        entry_num1.delete(0, tk.END)
        entry_num1.insert(tk.END, str(result))
    except Exception:
        entry_num1.delete(0, tk.END)
        entry_num1.insert(tk.END, "Error")

def tan():
    try:
        expression = entry_num1.get()
        result = math.tan(eval(expression))
        entry_num1.delete(0, tk.END)
        entry_num1.insert(tk.END, str(result))
    except Exception:
        entry_num1.delete(0, tk.END)
        entry_num1.insert(tk.END, "Error")

def button_click(number):
    current = entry_num1.get()
    entry_num1.delete(0, tk.END)
    entry_num1.insert(tk.END, str(current) + str(number))

def operator_click(operator):
    current = entry_num1.get()
    entry_num1.delete(0, tk.END)
    entry_num1.insert(tk.END, str(current) + str(operator))

def clear_input():
    entry_num1.delete(0, tk.END)

def calculate_result():
    try:
        expression = entry_num1.get()
        result = eval(expression)
        entry_num1.delete(0, tk.END)
        entry_num1.insert(tk.END, str(result))
    except Exception:
        entry_num1.delete(0, tk.END)
        entry_num1.insert(tk.END, "Error")

# Create the main application window
app = tk.Tk()
app.title("Calculator")
app.geometry("350x465")
app.configure(bg="grey")

# Create input field
entry_num1 = tk.Entry(app, width=20, font=("Helvetica", 20), justify=tk.RIGHT)
entry_num1.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Create number buttons
number_buttons = []
for number in range(1, 10):
    number_buttons.append(tk.Button(app, text=str(number), padx=20, pady=10, font=("Helvetica", 20),bg="yellow",
                                    command=lambda num=number: button_click(num)))

row_index = 1
col_index = 0
for button in number_buttons:
    button.grid(row=row_index, column=col_index, padx=5, pady=5, sticky='nsew')  # Add sticky='nsew' for equal size
    col_index += 1
    if col_index > 2:
        col_index = 0
        row_index += 1

# Create operator buttons
operator_buttons = ['+', '-', '*', '/']
row_index = 1
col_index = 3
for operator in operator_buttons:
    operator_button = tk.Button(app, text=operator, padx=20, pady=10, font=("Helvetica", 20),bg="green",
                                command=lambda op=operator: operator_click(op))
    operator_button.grid(row=row_index, column=col_index, padx=5, pady=5, sticky='nsew')  # Add sticky='nsew' for equal size
    row_index += 1

# Create other buttons
zero_button = tk.Button(app, text='0', padx=20, pady=10, font=("Helvetica", 20), bg="yellow",
                        command=lambda num=0: button_click(num))
zero_button.grid(row=4, column=0, padx=5, pady=5, sticky='nsew')  # Add sticky='nsew' for equal size

decimal_button = tk.Button(app, text='.', padx=20, pady=10, font=("Helvetica", 20),bg="white",
                           command=lambda: button_click('.'))
decimal_button.grid(row=4, column=1, padx=5, pady=5, sticky='nsew')  # Add sticky='nsew' for equal size

equal_button = tk.Button(app, text="=", padx=20, pady=10, font=("Helvetica", 20),bg="purple", command=calculate_result)
equal_button.grid(row=4, column=2, padx=5, pady=5, sticky='nsew')  # Add sticky='nsew' for equal size

clear_button = tk.Button(app, text="C", padx=20, pady=10, font=("Helvetica", 20),bg="red", command=clear_input)
clear_button.grid(row=5, column=0, padx=5, pady=5, sticky='nsew')  # Add sticky='nsew' for equal size

# Create trigonometric function buttons
cos_button = tk.Button(app, text="cos", padx=20, pady=10, font=("Helvetica", 20),bg="orange", command=cos)
cos_button.grid(row=5, column=1, padx=5, pady=5, sticky='nsew')  # Add sticky='nsew' for equal size

sin_button = tk.Button(app, text="sin", padx=20, pady=10, font=("Helvetica", 20),bg="orange", command=sin)
sin_button.grid(row=5, column=2, padx=5, pady=5, sticky='nsew')  # Add sticky='nsew' for equal size

tan_button = tk.Button(app, text="tan", padx=20, pady=10, font=("Helvetica", 20),bg="orange", command=tan)
tan_button.grid(row=5, column=3, padx=5, pady=5, sticky='nsew')  # Add sticky='nsew' for equal size

# Configure row and column weights to make the buttons expand equally
for i in range(5):
    app.grid_rowconfigure(i, weight=1)
for i in range(4):
    app.grid_columnconfigure(i, weight=1)

app.mainloop()