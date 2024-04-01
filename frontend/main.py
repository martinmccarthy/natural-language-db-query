import tkinter as tk
import sys
import os
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from backend.api import process_user_input

def submit_chat():
    user_input = entry.get()
    process_user_input(user_input) 
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Chat Input Example")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

entry = tk.Entry(frame, width=50)
entry.bind("<Return>", lambda event: submit_chat())
entry.pack(side=tk.LEFT, padx=(0, 10))

submit_button = tk.Button(frame, text="Submit", command=submit_chat)
submit_button.pack(side=tk.LEFT)

root.mainloop()
