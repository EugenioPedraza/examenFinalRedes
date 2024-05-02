from flask import Flask, request, send_file, jsonify
from cryptography.fernet import Fernet
from PIL import Image
import io
import base64

app = Flask(__name__)

@app.route('/', methods=['POST'])
def decrypt_image():
    data = request.json
    encrypted_data = base64.b64decode(data['encrypted_image'])
    key = base64.b64decode(data['key'])
    cipher = Fernet(key)
    
    try:
        decrypted_data = cipher.decrypt(encrypted_data)
        image = Image.open(io.BytesIO(decrypted_data))
        img_io = io.BytesIO()
        image.save(img_io, 'PNG')
        img_io.seek(0)
        return send_file(img_io, mimetype='image/png')
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)
