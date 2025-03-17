# FileLock

## Overview
FileLock is a simple file encryption and decryption tool that allows users to securely protect their files using a password. The application uses AES encryption via the `cryptography` library and provides a graphical user interface (GUI) using `Tkinter`.

## Features
- Encrypt any file with a password
- Decrypt files using the correct password
- Simple and intuitive GUI

## Requirements
Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

Install the required dependencies using:
```sh
pip install cryptography
```

## How to Use

1. Run the script using:
   ```sh
   python FileLock.py
   ```
2. Click **Encrypt File** and select the file you want to encrypt.
3. Enter a password when prompted.
4. The file will be encrypted and saved in the same location.
5. To decrypt, click **Decrypt File**, select the encrypted file, and enter the correct password.

## Security Note
- The encryption key is derived from the password using SHA-256 hashing.
- Make sure to remember your password, as files cannot be decrypted without it.

## License
This project is open-source and available under the MIT License.

## Author
Andrew Abercrombie.