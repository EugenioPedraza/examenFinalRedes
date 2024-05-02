import requests
from cryptography.fernet import Fernet
from PIL import Image
import io
import base64

# Genera la clave y el cifrador
key = Fernet.generate_key()
cipher = Fernet(key)

server_url = 'http://localhost:3000'

def encrypt_image(image_path):
    with Image.open(image_path) as img:
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        encrypted_data = cipher.encrypt(img_byte_arr.getvalue())
        return base64.b64encode(encrypted_data).decode('utf-8')

def send_encrypted_image(image_path):
    encrypted_image = encrypt_image(image_path)
    response = requests.post(server_url, json={'encrypted_image': encrypted_image, 'key': base64.b64encode(key).decode('utf-8')})
    if response.status_code == 200:
        with open('decrypted_image.png', 'wb') as f:
            f.write(response.content)
        print("Decrypted image saved successfully.")
    else:
        print("Failed to decrypt image:", response.json())

if __name__ == "__main__":
    send_encrypted_image('imagen.png')
