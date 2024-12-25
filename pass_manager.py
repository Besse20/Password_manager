import os
import base64
import sqlite3
from cryptography.fernet import Fernet
from getpass import getpass

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
    conn.commit()
    conn.close()

setup_database()

# Step 3: Core Functions
def add_password():
    website = input("Enter the website: ").strip()
    username = input("Enter the username: ").strip()
    password = getpass("Enter the password: ").strip()
    encrypted_password = cipher.encrypt(password.encode()).decode()

    conn = sqlite3.connect("password_manager.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)", 
                   (website, username, encrypted_password))
    conn.commit()
    conn.close()
    print("Password added successfully!")

def view_passwords():
    conn = sqlite3.connect("password_manager.db")
    cursor = conn.cursor()
    cursor.execute("SELECT website, username, password FROM passwords")
    rows = cursor.fetchall()
    conn.close()

    if rows:
        for row in rows:
            website, username, encrypted_password = row
            decrypted_password = cipher.decrypt(encrypted_password.encode()).decode()
            print(f"Website: {website}\nUsername: {username}\nPassword: {decrypted_password}\n{'-'*30}")
    else:
        print("No passwords stored.")

def delete_password():
    website = input("Enter the website to delete: ").strip()

    conn = sqlite3.connect("password_manager.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM passwords WHERE website = ?", (website,))
    conn.commit()
    conn.close()

    print(f"Password for {website} deleted (if it existed).")

# Step 4: User Interface
def main():
    while True:
        print("\nPassword Manager")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Delete Password")
        print("4. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            delete_password()
        elif choice == "4":
            print("Exiting Password Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
