import tkinter as tk
from tkinter import messagebox, scrolledtext

# Main window
root = tk.Tk()
root.title("Student Educational Details")
root.geometry("700x400")
root.config(bg='light green')

# Store students in a list
students = []

# Left frame for form
form_frame = tk.Frame(root, padx=10, pady=10)
form_frame.pack(side=tk.LEFT, fill=tk.Y)

# Right frame for list display
list_frame = tk.Frame(root, padx=10, pady=10)
list_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Labels and Entry widgets for student details
tk.Label(form_frame, text="Name:").grid(row=0, column=0, sticky=tk.W, pady=5)
name_entry = tk.Entry(form_frame, width=30)
name_entry.grid(row=0, column=1, pady=5)

tk.Label(form_frame, text="Roll Number:").grid(row=1, column=0, sticky=tk.W, pady=5)
roll_entry = tk.Entry(form_frame, width=30)
roll_entry.grid(row=1, column=1, pady=5)

tk.Label(form_frame, text="Class:").grid(row=2, column=0, sticky=tk.W, pady=5)
class_entry = tk.Entry(form_frame, width=30)
class_entry.grid(row=2, column=1, pady=5)

tk.Label(form_frame, text="Marks:").grid(row=3, column=0, sticky=tk.W, pady=5)
marks_entry = tk.Entry(form_frame, width=30)
marks_entry.grid(row=3, column=1, pady=5)

# Function to add student details
def add_student():
    name = name_entry.get().strip()
    roll = roll_entry.get().strip()
    clas = class_entry.get().strip()
    marks = marks_entry.get().strip()
    
    if not (name and roll and clas and marks):
        messagebox.showwarning("Input Error", "Please fill all fields")
        return
    
    student_info = f"Name: {name}, Roll: {roll}, Class: {clas}, Marks: {marks}"
    students.append(student_info)
    update_student_list()
    clear_form()

# Function to update the list display
def update_student_list():
    student_list.delete(1.0, tk.END)
    for idx, student in enumerate(students, start=1):
        student_list.insert(tk.END, f"{idx}. {student}\n")

# Function to clear form fields
def clear_form():
    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    class_entry.delete(0, tk.END)
    marks_entry.delete(0, tk.END)

# Buttons
add_button = tk.Button(form_frame, text="Add Student", command=add_student, width=15)
add_button.grid(row=4, column=0, pady=10)

clear_button = tk.Button(form_frame, text="Clear Form", command=clear_form, width=15)
clear_button.grid(row=4, column=1, pady=10)

# Scrollable text area to show student list
student_list = scrolledtext.ScrolledText(list_frame, width=50, height=20)
student_list.pack(fill=tk.BOTH, expand=True)

root.mainloop()
