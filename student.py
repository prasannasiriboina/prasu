import tkinter as tk
from tkinter import messagebox

def calculate_average():
    try:
        name = entry_name.get()
        grade1 = float(entry_grade1.get())
        grade2 = float(entry_grade2.get())
        grade3 = float(entry_grade3.get())
        
        average = (grade1 + grade2 + grade3) / 3
        
        # Simple pass/fail based on average >= 60
        if average >= 60:
            result = f"{name} passed with an average grade of {average:.2f}"
        else:
            result = f"{name} failed with an average grade of {average:.2f}"
        
        label_result.config(text=result)
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers for grades.")

# Create main window
root = tk.Tk()
root.title("Student Grades")

# Labels and entries for name and grades
tk.Label(root, text="Student Name:").grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Grade 1:").grid(row=1, column=0, padx=5, pady=5)
entry_grade1 = tk.Entry(root)
entry_grade1.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Grade 2:").grid(row=2, column=0, padx=5, pady=5)
entry_grade2 = tk.Entry(root)
entry_grade2.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Grade 3:").grid(row=3, column=0, padx=5, pady=5)
entry_grade3 = tk.Entry(root)
entry_grade3.grid(row=3, column=1, padx=5, pady=5)

# Button to calculate
btn_calculate = tk.Button(root, text="Calculate Average", command=calculate_average)
btn_calculate.grid(row=4, column=0, columnspan=2, pady=10)

# Label to show result
label_result = tk.Label(root, text="")
label_result.grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()
