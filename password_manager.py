import os
import sqlite3
import hashlib
from cryptography.fernet import Fernet
from tkinter import Tk, Label, Entry, Button, Text, END, messagebox

# Step 1: Generate or Load Encryption Key
def load_or_create_key():
    key_file = "key.key"
    if not os.path.exists(key_file):
        key = Fernet.generate_key()
        with open(key_file, 'wb') as file:
            file.write(key)
    else:
        with open(key_file, 'rb') as file:
            key = file.read()
    return key

def get_cipher():
    key = load_or_create_key()
    return Fernet(key)

cipher = get_cipher()

# Step 2: Database Setup
def setup_database():
    conn = sqlite3.connect("password_manager.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS passwords (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        website TEXT NOT NULL,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS master_password (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        password_hash TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

setup_database()

# Step 3: Master Password Functions
def check_master_password():
    master_password = master_password_entry.get().strip()
    if not master_password:
        messagebox.showerror("Error", "Please enter your master password!")
        return False

    password_hash = hashlib.sha256(master_password.encode()).hexdigest()

    conn = sqlite3.connect("password_manager.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash FROM master_password WHERE id = 1")
    stored_hash = cursor.fetchone()
    conn.close()

    if stored_hash and stored_hash[0] == password_hash:
        return True
    else:
        messagebox.showerror("Error", "Incorrect master password!")
        return False

def set_master_password():
    master_password = master_password_entry.get().strip()
    if not master_password:
        messagebox.showerror("Error", "Please enter a master password!")
        return

    password_hash = hashlib.sha256(master_password.encode()).hexdigest()

    conn = sqlite3.connect("password_manager.db")
    cursor = conn.cursor()

    # Check if master password is already set
    cursor.execute("SELECT * FROM master_password WHERE id = 1")
    existing_master = cursor.fetchone()

    if existing_master:
        messagebox.showerror("Error", "Master password is already set!")
    else:
        cursor.execute("INSERT INTO master_password (password_hash) VALUES (?)", (password_hash,))
        conn.commit()
        messagebox.showinfo("Success", "Master password set successfully!")

    conn.close()

def view_passwords():
    if not check_master_password():
        return  # Return early if the master password is incorrect

    conn = sqlite3.connect("password_manager.db")
    cursor = conn.cursor()
    cursor.execute("SELECT website, username, password FROM passwords")
    rows = cursor.fetchall()
    conn.close()

    output_text.delete(1.0, END)
    if rows:
        for row in rows:
            website, username, encrypted_password = row
            decrypted_password = cipher.decrypt(encrypted_password.encode()).decode()
            output_text.insert(END, f"Website: {website}\nUsername: {username}\nPassword: {decrypted_password}\n{'-'*30}\n")
    else:
        output_text.insert(END, "No passwords stored.")

def add_password():
    if not check_master_password():
        return

    website = website_entry.get().strip()
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if not website or not username or not password:
        messagebox.showerror("Error", "All fields must be filled out!")
        return

    encrypted_password = cipher.encrypt(password.encode()).decode()

    conn = sqlite3.connect("password_manager.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)", 
                   (website, username, encrypted_password))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Password added successfully!")
    website_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)

def delete_password():
    if not check_master_password():
        return

    website = website_entry.get().strip()

    if not website:
        messagebox.showerror("Error", "Please enter the website to delete!")
        return

    conn = sqlite3.connect("password_manager.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM passwords WHERE website = ?", (website,))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", f"Password for {website} deleted (if it existed).")
    website_entry.delete(0, END)

# Step 4: GUI Setup
root = Tk()
root.title("Password Manager")

# Master Password Setup
Label(root, text="Set Master Password:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
master_password_entry = Entry(root, width=30, show="*")
master_password_entry.grid(row=0, column=1, padx=10, pady=5)

Button(root, text="Set Master Password", command=set_master_password).grid(row=1, column=0, columnspan=2, pady=10)

# Password Entry Fields
Label(root, text="Website:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
Label(root, text="Username:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
Label(root, text="Password:").grid(row=4, column=0, padx=10, pady=5, sticky="e")

website_entry = Entry(root, width=30)
website_entry.grid(row=2, column=1, padx=10, pady=5)

username_entry = Entry(root, width=30)
username_entry.grid(row=3, column=1, padx=10, pady=5)

password_entry = Entry(root, width=30, show="*")
password_entry.grid(row=4, column=1, padx=10, pady=5)

# Buttons
Button(root, text="Add Password", command=add_password).grid(row=5, column=0, columnspan=2, pady=10)
Button(root, text="View Passwords", command=view_passwords).grid(row=6, column=0, columnspan=2, pady=10)
Button(root, text="Delete Password", command=delete_password).grid(row=7, column=0, columnspan=2, pady=10)

# Output Area
output_text = Text(root, width=50, height=10, wrap="word")
output_text.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
