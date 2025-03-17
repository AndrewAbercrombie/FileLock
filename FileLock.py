import os
import base64
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import hashlib
from cryptography.fernet import Fernet

def generate_key_from_password(password: str):
    key = hashlib.sha256(password.encode()).digest()
    return Fernet(base64.urlsafe_b64encode(key[:32]))

def encrypt_file():
    password = simpledialog.askstring("Password", "Enter encryption password:", show='*')
    if not password:
        return
    
    cipher = generate_key_from_password(password)
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = cipher.encrypt(file_data)
    
    with open(file_path, "wb") as file:
        file.write(encrypted_data)
    
    messagebox.showinfo("Success", f"File encrypted: {file_path}")

def decrypt_file():
    password = simpledialog.askstring("Password", "Enter decryption password:", show='*')
    if not password:
        return
    
    cipher = generate_key_from_password(password)
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    
    try:
        decrypted_data = cipher.decrypt(encrypted_data)
        with open(file_path, "wb") as file:
            file.write(decrypted_data)
        messagebox.showinfo("Success", f"File decrypted: {file_path}")
    except:
        messagebox.showerror("Error", "Decryption failed. Invalid password or file.")

root = tk.Tk()
root.title("File Encryptor/Decryptor")
root.geometry("300x150")

tk.Button(root, text="Encrypt File", command=encrypt_file, width=20).pack(pady=10)
tk.Button(root, text="Decrypt File", command=decrypt_file, width=20).pack(pady=10)
tk.Button(root, text="Exit", command=root.quit, width=20).pack(pady=10)

root.mainloop()