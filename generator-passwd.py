import string
import random
import tkinter as tk
from tkinter import ttk

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation
generate = letters + numbers + symbols

length = 20

password = "".join(random.sample(generate, length))

# print(password) Console mode deactivated
version = "0.0.0.1.3"
# create a window
root = tk.Tk()
print("Welcome on Password Generator")
print("Developped by : Noxious")
print("Gen-Version: " + version)
name = input("Enter your name : ")
# size of the window
root.geometry("450x250")

# window title
root.title("Password Generator | Developed by : Noxious")

# main text
tk.Label(text="Welcome " + name + ", This is your password:", foreground="red", background="grey", width=100, font="Arial").pack()
tk.Label(text=f"{password}", background="grey", width="100", height="50", foreground="red", font="Arial").pack()

# Main loop
root.mainloop()
# Next Update : GUI Update : Better design
