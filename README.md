# Password_manager

This is a simple and secure command-line Password Manager application written in Python. It enables users to securely store, retrieve, and delete their passwords for various websites. Passwords are encrypted using the `Fernet` encryption from the `cryptography` library.

---

## Features
- **Add Passwords**: Store website credentials (username and password).
- **View Passwords**: Retrieve and decrypt stored passwords.
- **Delete Passwords**: Remove credentials for a specified website.
- **Encryption**: All passwords are securely encrypted before being stored.
- **Database Storage**: Uses SQLite for efficient and lightweight storage.

---

## Prerequisites
Ensure the following are installed on your system:
- **Python 3.x**
- **Required Python Libraries**:
  - `cryptography`

To install the necessary library, run:
```bash
pip3 install cryptography
```

---

## Installation
1. Clone or download this repository.
2. Navigate to the directory containing the script.
3. Run the following command to start the application:
   ```bash
   python3 password_manager.py
   ```

---

## Usage

### Menu Options
When you run the application, you will see a menu:
```
Password Manager
1. Add Password
2. View Passwords
3. Delete Password
4. Exit
```

### Adding a Password
- Choose option `1` from the menu.
- Enter the following information when prompted:
  - Website name
  - Username
  - Password (input is hidden for security).
- The credentials will be encrypted and stored in the database.

### Viewing Passwords
- Choose option `2` from the menu.
- All stored credentials will be displayed with decrypted passwords.

### Deleting a Password
- Choose option `3` from the menu.
- Enter the website name for which the credentials should be deleted.
- If the website exists in the database, the corresponding credentials will be removed.

### Exiting the Application
- Choose option `4` to exit the program.

---

## File Structure
- **`password_manager.py`**: The main script file for the application.
- **`key.key`**: Automatically generated file that stores the encryption key (created on first run).
- **`password_manager.db`**: SQLite database file where encrypted passwords are stored (created on first run).

---

## Security
- **Encryption**: All passwords are encrypted using the `Fernet` symmetric encryption.
- **Encryption Key**: The `key.key` file is required for decryption. Do not share or lose this file.

---

## Future Enhancements
- Add a master password for accessing the application.
- Implement a password generator.
- Create a graphical user interface (GUI).
- Add data export/import functionality.

---

## License
This project is licensed under the MIT License. Feel free to modify and use it as needed.

---

## Acknowledgments
This project uses the `cryptography` library for encryption and `sqlite3` for database management.

should you have any questions don't hasitate to ask:
linkedin: https://www.linkedin.com/in/besufekad-terefe-34527a197/
Telegram:t.me/besufekadd
instagram: instagram.com/besse.cs

