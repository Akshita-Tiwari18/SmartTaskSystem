import tkinter as tk
from tkinter import messagebox
import os
import pandas as pd

# Function to organize files (just for demonstration)
def organize_files():
    folder_path = entry.get()
    if not os.path.exists(folder_path):  # Check if the path exists
        messagebox.showerror("Error", "Invalid Path!")
    else:
        messagebox.showinfo("Info", f"Organizing files in {folder_path}...")

# Function to add a task (just for demonstration)
def add_task():
    task_name = task_name_entry.get()
    priority = priority_entry.get()
    if task_name and priority:
        # Append to tasks.csv (assuming CSV handling is already implemented)
        tasks = pd.read_csv("tasks.csv")
        tasks = tasks.append({"Task": task_name, "Priority": priority}, ignore_index=True)
        tasks.to_csv("tasks.csv", index=False)
        messagebox.showinfo("Success", f"Task '{task_name}' added successfully!")
    else:
        messagebox.showerror("Error", "Please enter both task name and priority.")

# Main GUI window
root = tk.Tk()
root.title("Smart Automation System")

# Frame for organizing files
organize_frame = tk.LabelFrame(root, text="Organize Files", padx=10, pady=10)
organize_frame.pack(padx=20, pady=10)

label = tk.Label(organize_frame, text="Enter Folder Path:")
label.grid(row=0, column=0)

entry = tk.Entry(organize_frame, width=40)
entry.grid(row=0, column=1)

organize_button = tk.Button(organize_frame, text="Organize Files", command=organize_files)
organize_button.grid(row=1, column=0, columnspan=2, pady=10)

# Frame for adding a task
task_frame = tk.LabelFrame(root, text="Add New Task", padx=10, pady=10)
task_frame.pack(padx=20, pady=10)

task_name_label = tk.Label(task_frame, text="Task Name:")
task_name_label.grid(row=0, column=0)

task_name_entry = tk.Entry(task_frame, width=40)
task_name_entry.grid(row=0, column=1)

priority_label = tk.Label(task_frame, text="Priority (1=High, 5=Low):")
priority_label.grid(row=1, column=0)

priority_entry = tk.Entry(task_frame, width=40)
priority_entry.grid(row=1, column=1)

add_task_button = tk.Button(task_frame, text="Add Task", command=add_task)
add_task_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the GUI
root.mainloop()
