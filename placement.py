import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    course = entry_course.get()

    if name == "" or email == "" or phone == "" or course == "":
        messagebox.showwarning("Input Error", "Please fill all fields!")
    else:
        messagebox.showinfo("Registration Success", f"Thank you {name}!\nYou are registered for {course} placement.")
        # Clear fields after submission
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_course.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Placement Registration")
root.geometry("350x300")

# Labels and entries
tk.Label(root, text="Name:").pack(pady=(10,0))
entry_name = tk.Entry(root, width=30)
entry_name.pack()

tk.Label(root, text="Email:").pack(pady=(10,0))
entry_email = tk.Entry(root, width=30)
entry_email.pack()

tk.Label(root, text="Phone:").pack(pady=(10,0))
entry_phone = tk.Entry(root, width=30)
entry_phone.pack()

tk.Label(root, text="Course:").pack(pady=(10,0))
entry_course = tk.Entry(root, width=30)
entry_course.pack()

# Submit button
submit_btn = tk.Button(root, text="Register", command=submit_form)
submit_btn.pack(pady=20)

root.mainloop()
