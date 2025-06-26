# Password Manager

A simple and secure password manager built with Python, using encryption to protect sensitive information. The application features a graphical user interface (GUI) built with `Tkinter` for managing and retrieving passwords securely.

--- (besse)

## Features
- **Master Password Protection**: Safeguards access to all stored passwords.
- **Encrypted Password Storage**: Utilizes the `cryptography` library for secure encryption of passwords.
- **Add Passwords**: Save website credentials securely.
- **View Passwords**: Retrieve stored passwords (requires master password authentication).
- **Delete Passwords**: Remove stored credentials by specifying the website.
- **Persistent Storage**: Passwords are stored in an SQLite database.

---

## Prerequisites
- Python 3.6 or higher
- Required Python libraries:
  - `cryptography`
  - `sqlite3` (built-in)
  - `tkinter` (built-in)
  - `hashlib` (built-in)

To install the `cryptography` library, run:
```bash
pip install cryptography
```

---

## Getting Started

### 1. Clone or Download the Repository
```bash
https://github.com/Besse20/Password_manager.git
cd password_manager
```

### 2. Run the Application
```bash
python password_manager.py
```

---

## How to Use

### **Set the Master Password**
1. On the first run, set a master password.
2. This master password will be hashed and stored securely in the database.
3. You will need this password to view, add, or delete credentials.

### **Add Passwords**
1. Fill in the website, username, and password fields.
2. Click **"Add Password"** to save the credentials securely.

### **View Passwords**
1. Enter your master password.
2. Click **"View Passwords"** to display the stored credentials in the text area.

### **Delete Passwords**
1. Enter your master password.
2. Specify the website whose credentials you want to delete.
3. Click **"Delete Password"**.

---

## Security Considerations
- Passwords are encrypted using the `cryptography.fernet` symmetric encryption algorithm.
- The master password is hashed using SHA-256 for secure storage.
- Ensure the `key.key` file is kept secure, as it is essential for decrypting your passwords.

---

## Known Issues
- Deleting a password requires an exact match of the website name.
- Currently, there is no option to reset the master password.

---

## Future Improvements
- Implement a master password recovery option.
- Enhance the GUI for a more user-friendly experience.
- Add support for exporting/importing passwords.

---

## Contributing
Pull requests are welcome. For significant changes, please open an issue to discuss what you would like to change.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Socials

Linkedin: https://www.linkedin.com/in/besufekad-terefe-34527a197/

Instagram: https://instagram.com/besse.cs

Telegram: https://t.me/besufekadd
