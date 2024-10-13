import tkinter as tk 
root = tk.Tk()
root.title("Password Manager")
root.geometry("400x300")
root.resizable(0,0)

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
save_button = tk.Button(root, text="Save Password")
save_button.pack(pady=5)

retrive_button = tk.Button(root, text="Retrive Password")
retrive_button.pack(pady=5)

display_button = tk.Button(root, text="View all Passwords")
display_button.pack(pady=5)


root.mainloop()