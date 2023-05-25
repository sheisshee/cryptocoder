import tkinter as tk
from tkinter import filedialog

# Function to encrypt a message using Caesar Cipher
def encrypt(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((ord(char) + key - 65) % 26 + 65)
            else:
                encrypted_char = chr((ord(char) + key - 97) % 26 + 97)
        else:
            encrypted_char = char
        encrypted_message += encrypted_char
    return encrypted_message

# Function to decrypt a message using Caesar Cipher
def decrypt(message, key):
    return encrypt(message, 26 - key)

# Function to handle file selection for encryption
def select_file_encrypt():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            message = file.read()
        key = int(key_entry.get())
        encoded_message = encrypt(message, key)
        encoded_text.delete("1.0", tk.END)
        encoded_text.insert(tk.END, encoded_message)
        encoded_save_button.config(state=tk.NORMAL)

# Function to handle file selection for decryption
def select_file_decrypt():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            encoded_message = file.read()
        key = int(key_entry.get())
        decoded_message = decrypt(encoded_message, key)
        decoded_text.delete("1.0", tk.END)
        decoded_text.insert(tk.END, decoded_message)

# Function to save the encoded message to a file
def save_encoded_file():
    encoded_message = encoded_text.get("1.0", tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(encoded_message)
        status_label.config(text="Encoded file saved successfully.")

# Create the GUI window
window = tk.Tk()
window.title("Encoder/Decoder")
window.configure(bg="#565656")  # Set window background color

# Create a header label
header = tk.Label(window, text="Caesar Cipher", font=("Century", 18), width=30, highlightbackground="gray", highlightthickness=5, relief="groove")
header.pack(pady=2)

# Create the label for the key input
key_label = tk.Label(window, text="Enter the key:", padx=15, pady=2, bg="lightgray", relief="raised")
key_label.pack()

# Create the entry field for the key
key_entry = tk.Entry(window, width=10, font=("Century", 12))
key_entry.pack(pady=5)

# Create the button to select file for encryption
encrypt_button = tk.Button(window, text="Select File to Encrypt", command=select_file_encrypt, bg="gray", fg="white")
encrypt_button.pack(pady=2)

# Create the button to select file for decryption
decrypt_button = tk.Button(window, text="Select File to Decrypt", command=select_file_decrypt, bg="gray", fg="white")
decrypt_button.pack(pady=2)

# Create the label and text widget for the encoded text
encoded_label = tk.Label(window, text="Encoded Text:", font=("Century", 10), width=15, highlightbackground="gray", highlightthickness=2, relief="groove")
header.pack(pady=2)
encoded_label.pack(pady=2)
encoded_text = tk.Text(window, height=10, width=50, font=("Century", 10))
encoded_text.pack()

# Create the button to save the encoded file
encoded_save_button = tk.Button(window, text="Save Encoded File", font=("Century", 8), state=tk.DISABLED, command=save_encoded_file, bg="white", fg="black")
encoded_save_button.pack(pady=2)

# Create the label and text widget for the decoded text
decoded_label = tk.Label(window, text="Decoded Text:", font=("Century", 10), width=15, highlightbackground="gray", highlightthickness=2, relief="groove")
decoded_label.pack(pady=2)
decoded_text = tk.Text(window, height=10, width=50, font=("Century", 10))
decoded_text.pack()

# Create a box (label) with margins
box = tk.Label(window, text="@2023 by G-32", padx=5, pady=5)
box.pack(pady=2)

# Create a label widget with initial background color
label = tk.Label(window, text=" ", width=300, height=300)
label.pack()

# Run the GUI window
window.mainloop()

