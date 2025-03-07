import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        selected_task = task_list.curselection()[0]
        task_list.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete!")

def mark_done():
    try:
        selected_task = task_list.curselection()[0]
        task = task_list.get(selected_task)
        task_list.delete(selected_task)
        task_list.insert(tk.END, f"✔ {task}")  # Mark completed
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to mark as done!")

# Create main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")
root.config(bg="#2c3e50")

# Title
title_label = tk.Label(root, text="To-Do List", font=("Arial", 18, "bold"), fg="white", bg="#2c3e50")
title_label.pack(pady=10)

# Task Entry
task_entry = tk.Entry(root, font=("Arial", 14), width=30)
task_entry.pack(pady=5)

# Buttons
button_frame = tk.Frame(root, bg="#2c3e50")
button_frame.pack(pady=5)

add_button = tk.Button(button_frame, text="Add", command=add_task, font=("Arial", 12), width=8, bg="#27ae60", fg="white")
add_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(button_frame, text="Delete", command=delete_task, font=("Arial", 12), width=8, bg="#e74c3c", fg="white")
delete_button.grid(row=0, column=1, padx=5)

done_button = tk.Button(button_frame, text="Done", command=mark_done, font=("Arial", 12), width=8, bg="#f39c12", fg="white")
done_button.grid(row=0, column=2, padx=5)

# Task List
task_list = tk.Listbox(root, font=("Arial", 12), width=40, height=15, bg="#34495e", fg="white", selectbackground="#95a5a6")
task_list.pack(pady=10)

root.mainloop()
