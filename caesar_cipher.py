from flask import Flask, render_template, request
import random

app = Flask(__name__)

def encrypt(text, key):

    # Encrypts the given text using a Caesar Cipher.

    encrypted = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)
        else:
            encrypted += char
    return encrypted

def decrypt(text, key):

    # Decrypts the given text by reversing the Caesar Cipher.

    return encrypt(text, -key)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    key = None
    if request.method == 'POST':
        mode = request.form.get('mode')
        message = request.form.get('message')
        
        if mode == 'encrypt':
            key = random.randint(1, 25)  # Generate a random key for decryption
            result = encrypt(message, key)
        elif mode == 'decrypt':
            try:
                key = int(request.form.get('key'))
                result = decrypt(message, key)
            except (ValueError, TypeError):
                result = "Invalid Key for decryption."
    
    return render_template('index.html', result=result, key=key)

if __name__ == '__main__':
    app.run(debug=True)
