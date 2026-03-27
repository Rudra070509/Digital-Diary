import tkinter as tk
from tkinter import messagebox

# function to check login
def login():
    username = entry_user.get()
    password = entry_pass.get()

    if username == "admin" and password == "1234":
        messagebox.showinfo("Login", "Login Successful!")
    else:
        messagebox.showerror("Login", "Invalid Username or Password")

# create window
root = tk.Tk()
root.title("Digital Diary Login")
root.geometry("300x200")

# username label + input
tk.Label(root, text="Username").pack()
entry_user = tk.Entry(root)
entry_user.pack()

# password label + input
tk.Label(root, text="Password").pack()
entry_pass = tk.Entry(root, show="*")  # hides password
entry_pass.pack()

# login button
tk.Button(root, text="Login", command=login).pack(pady=10)

# run app
root.mainloop()