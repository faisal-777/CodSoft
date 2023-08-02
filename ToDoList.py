import tkinter as tk

tasks = []

def add_task():
    title_label.config(text="Enter the task :", bg="black", fg="white")
    title_entry.delete(0, tk.END)
    title_entry.pack(pady=10)
    save_button.config(text="Save", command=save_task, bg="black", fg="white")
    save_button.pack(pady=10)

def save_task():
    title = title_entry.get()
    if title:
        task = {"title": title, "completed": False}
        tasks.append(task)
        refresh_list()

def mark_completed():
    selected_index = task_listbox.curselection()
    if selected_index:
        index = selected_index[0]
        tasks[index]["completed"] = True
        refresh_list()

def delete_task():
    selected_index = task_listbox.curselection()
    if selected_index:
        index = selected_index[0]
        del tasks[index]
        refresh_list()

def edit_task():
    selected_index = task_listbox.curselection()
    if selected_index:
        index = selected_index[0]
        task = tasks[index]

        title_label.config(text="Edit the task :", bg="black", fg="white")
        title_entry.delete(0, tk.END)
        title_entry.insert(0, task["title"])
        title_entry.pack(pady=10)
        save_button.config(text="Save", command=lambda: save_edited_task(index), bg="yellow")
        save_button.pack(pady=10)

def save_edited_task(index):
    title = title_entry.get()
    if title:
        tasks[index]["title"] = title
        refresh_list()

def refresh_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = " (Completed)" if task["completed"] else ""
        task_listbox.insert(tk.END, f"{task['title']}{status}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("To-Do List App")
    root.configure(bg="purple")

    title_label = tk.Label(root, text="To-Do List", font=("Helvetica", 18, "bold"))
    title_label.pack(pady=10)

    task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=15, font=("Helvetica", 12, "bold"))
    task_listbox.pack()

    title_entry = tk.Entry(root, font=("Helvetica", 12))
    save_button = tk.Button(root, text="Save", command=save_task, font=("Helvetica", 12, "bold"), bg="black", fg="white")
    
    add_task_button = tk.Button(root, text="Add Task", command=add_task, font=("Helvetica", 12, "bold"), bg="black", fg="white")
    add_task_button.pack(pady=5)

    complete_button = tk.Button(root, text="Mark as Completed", command=mark_completed, font=("Helvetica", 12, "bold"), bg="green", fg="white")
    complete_button.pack(pady=5)

    delete_button = tk.Button(root, text="Delete Task", command=delete_task, font=("Helvetica", 12, "bold"), bg="red", fg="white")
    delete_button.pack(pady=5)

    edit_button = tk.Button(root, text="Edit Task", command=edit_task, font=("Helvetica", 12, "bold"), bg="yellow")
    edit_button.pack(pady=5)

    refresh_list()  # To populate the task_listbox initially

    root.mainloop()
