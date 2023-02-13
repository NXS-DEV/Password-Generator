import string
import secrets
import tkinter as tk
from tkinter import ttk

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation
generate = letters + numbers + symbols

length = 20  # add your own password_length

password = "".join(secrets.choice(generate) for i in range(length))

# gen-version
version = "0.0.0.1.4"
print("Welcome on Password Generator")
print("Developed by : Noxious")
print("Gen-Version: " + version)
name = input("Enter your name : ")
print(password)

# create a window
root = tk.Tk()

# size of the window
root.geometry("450x250")

# window title
root.title("Password Generator | Developed by : Noxious")

# main text
tk.Label(text="Welcome " + name + f",\n This is your password: {password} ", foreground="green",
         background="grey", width=100, font="Arial").pack()

# first button
reset_btn = ttk.Button(root, text="RESET", command=lambda: generate_password(length))
# second button
copy_btn = ttk.Button(root, text="Copy Password", command=None)

reset_btn.pack(ipadx=5, ipady=5, expand=True)
copy_btn.pack(ipadx=4, ipady=4, expand=True)

def generate_password(length):
    global password
    password = "".join(secrets.choice(generate) for i in range(length))
    tk.Label(root, text=f"Your new password is: {password}", foreground="green", background="grey", width=100, font="Arial").pack()

# window update
root.update()
# Main loop
root.mainloop()
