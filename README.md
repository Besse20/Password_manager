Password Manager


This is a simple password manager application that allows users to store and manage passwords securely using encryption and a master password. The application uses SQLite for storage and Fernet symmetric encryption for password security.

Features:



Set Master Password: Secure your password manager with a master password.


Add Passwords: Store website, username, and password securely.


View Passwords: View saved passwords (after entering the correct master password).


Delete Password: Remove saved passwords by specifying the website.


Requirements



Python 3.x


cryptography library (for encryption)


sqlite3 library (for database storage)


tkinter library (for GUI)


Installation



1. Clone the repository

bash

Copy code

git clone https://github.com/yourusername/password-manager.git


cd password-manager


2. Install dependencies


Make sure you have the required dependencies installed.


 You can install them using pip:

bash

Copy code

pip install cryptography


3. Run the application


To run the password manager, simply execute the script:

bash

Copy code

python password_manager.py

How to Use

1. Set the Master Password

When the application starts, you'll be prompted to set a master password. This password will be used to protect your saved passwords.

The master password is securely hashed before being stored in the database.

2. Add a Password

To add a password, fill out the website, username, and password fields.

The password will be encrypted before being saved in the database.

3. View Saved Passwords

To view saved passwords, enter the correct master password.

All saved passwords will be decrypted and displayed in the application.

4. Delete a Password

To delete a password, enter the website's name and click "Delete Password".

The password for the specified website will be removed from the database.

Database Structure

The application uses an SQLite database (password_manager.db) with the following tables:


master_password: Stores the hashed master password.


id: Primary Key (integer)

password_hash: Hashed master password (string)

passwords: Stores the encrypted passwords for each website.



id: Primary Key (integer)

website: Website name (string)

username: Username (string)

password: Encrypted password (string)

Security

Encryption: The passwords are encrypted using the cryptography library's Fernet symmetric encryption scheme. The encryption key is stored in a separate file (key.key), and the key is loaded at runtime.

Master Password: The master password is hashed using SHA-256 before being stored in the database.

Troubleshooting

Master Password Issue: If you forget your master password, there's no way to recover it. You will need to reset the password manager by deleting the database file (password_manager.db) and starting over.



Key File Missing: If the key.key file is deleted or missing, you won't be able to decrypt stored passwords. It's important to keep the encryption key file safe.



License

This project is licensed under the MIT License - see the LICENSE file for details.

