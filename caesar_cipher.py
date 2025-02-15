from flask import Flask, render_template, request
import random

app = Flask(__name__)

def encrypt(text, shift):
    """
    Encrypts the given text using a Caesar Cipher with the random shift.
    """
    encrypted = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            encrypted += char
    return encrypted

def decrypt(text, shift):
    """
    Decrypts the given text by reversing the Caesar Cipher shift.
    """
    return encrypt(text, -shift)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    shift = None
    if request.method == 'POST':
        mode = request.form.get('mode')
        message = request.form.get('message')
        
        if mode == 'encrypt':
            shift = random.randint(1, 25)  # Generate a random shift value
            result = encrypt(message, shift)
        elif mode == 'decrypt':
            try:
                shift = int(request.form.get('shift'))
                result = decrypt(message, shift)
            except (ValueError, TypeError):
                result = "Invalid shift value for decryption."
    
    return render_template('index.html', result=result, shift=shift, mode=request.form.get('mode'))

if __name__ == '__main__':
    app.run(debug=True)
    
