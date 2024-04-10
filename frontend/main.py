import tkinter as tk
import sys
import os
import requests

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

def submit_chat():
    user_input = entry.get()
    prompt = "You are a SQL Engineer, you have a database with the following: \n"
    prompt += "Table: Customer_Data\n"
    prompt += "Columns: uuid, name, email, zip_code, phone, birthday, salary, subscription_type, credit_score, dependents\n"
    prompt += "You have been tasked with writing queries based on plain english. Take the english given to you and convert it into a SQL query.\n"
    prompt += "Never respond with more information other than a SQL query. You can assume the database is already populated with data.\n"
    prompt += "For example, if the user says 'Show me all the customers with a salary greater than 50000', you should convert that into a SQL query and return the results.\n"

    response = requests.get(f"http://localhost:8000/chat", params={'message': user_input, 'prompt': prompt})
    print(response.text)
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
