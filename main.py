import tkinter as tk
import json
import os
from tkinter import messagebox
root = tk.Tk()
root.title("Password Manager")
root.geometry("400x300")
root.resizable(0,0)

def save():
    website = web_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    append_data = {
        website: {
            "username": username,
            "password": password
        }
    }
    if os.path.exists("password.json"):
        with open("password.json", "r") as file:
            data = json.load(file)
            data.update(append_data)
    else:
        data = append_data
    with open("password.json","w") as file:
        json.dump(data,file,indent=4)
        messagebox.showinfo("Successful", "The following password has been saved")
    web_entry.delete(0,tk.END)
    username_entry.delete(0,tk.END)
    password_entry.delete(0,tk.END)

def retrive():
    if os.path.exists("password.json"):
        with open("password.json", "r") as file:
            data = json.load(file)
            website = web_entry.get()
            if website in data:
                username = data[website]["username"]
                password = data[website]["password"]
                messagebox.showinfo("Password",f"Website: {website}\nUsername: {username}\nPassword: {password}")
            else:
                messagebox.showerror("Error"," Please provide the input field for the website")
    else:
        messagebox.showerror("Error","There is no saved password")
    username_entry.delete(0, tk.END)

def show():
    if os.path.exists("password.json"):
        with open("password.json","r") as file:
            data= json.load(file)
            credential =""
            for key,value in data.items():
                username = value.get("username")
                password = value.get("password")
                credential += f"Website: {key}\nUsername: {username}\nPassword: {password}\n\n"
            messagebox.showinfo("Passwords" ,credential)
    else:
        messagebox.showerror("Error","There is no saved passwords")
#creating input field
Web_label = tk.Label(root,text="Website:") 
Web_label.pack(pady=5)
web_entry = tk.Entry(root,width=40)
web_entry.pack(pady=5)

username_label = tk.Label(root,text="Username:") 
username_label.pack(pady=5)
username_entry = tk.Entry(root,width=40)
username_entry.pack(pady=5)

password_label = tk.Label(root,text="Password:") 
password_label.pack(pady=5)
password_entry = tk.Entry(root,width=40)
password_entry.pack(pady=5)

#creating buttons for saving, retriving and displaying all passwords. 
save_button = tk.Button(root, text="Save Password", command=save)
save_button.pack(pady=5)

retrive_button = tk.Button(root, text="Retrive Password", command=retrive)
retrive_button.pack(pady=5)

display_button = tk.Button(root, text="View all Passwords",command=show)
display_button.pack(pady=5)


root.mainloop()