Overview:
This is a simple Password Manager application built using Python's Tkinter GUI and Cryptography for password encryption and storage. The program allows you to securely store, retrieve, and view passwords for different websites. Passwords are encrypted and saved in a local JSON file for security, and the encryption key is stored in a separate file.

Features:
Save Passwords: Store passwords for different websites, along with usernames.
Retrieve Passwords: Retrieve the username and decrypted password for a specific website.
View All Passwords: Display all stored usernames and passwords.
Encryption: Passwords are encrypted using the Fernet symmetric encryption from the cryptography library.

Installation:
Clone or download the project files to your local machine.
Install required Python libraries by running the following command in your terminal
- pip install cryptography

Functionality:
Save a Password:
Enter a website name, username, and password in the respective fields.
Click the "Save Password" button.
The encrypted password will be saved in a file named password.json.

Retrieve a Password:
Enter the website name and click the "Retrieve Password" button.
If the website exists in the saved data, the username and decrypted password will be displayed in a pop-up message box.

View All Passwords:
Click the "View all Passwords" button.
A pop-up window will display all stored websites along with their usernames and decrypted passwords.

Files:
password_manager.py: Main Python script for the Password Manager.
password.json: JSON file where encrypted passwords are stored.
key.txt: A file that stores the encryption key for the Fernet encryption.

Encryption Details:
Fernet Encryption: This uses symmetric encryption to both encrypt and decrypt the password data.
The encryption key is generated once and saved in a key.txt file. This key is crucial for retrieving and decrypting stored passwords.

Dependencies:
tkinter: For the graphical user interface.
json: To read/write passwords in the JSON format.
cryptography (Fernet): To securely encrypt and decrypt passwords.
os: To check file existence for key and password storage.