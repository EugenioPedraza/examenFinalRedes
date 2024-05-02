El codigo corre en Python3 y es necesario descargar y/o importar las siguientes librerias:
- Flask
- Cryptography
- Requests
- Image
- io
- base64

Para poder correr el codigo simplemente es necesario PRIMERO correr el main.py (python3 main.py) y despues cliente.py (python3 cliente.py)

Al momento de correr el servidor estara esperando una respuesta (metodo POST) en donde cuando se corra el archivo de cliente se encryptara la imagen y se enviara la imagen encriptada y la llave de desencriptacion. Cuando el servidor lo reciba hara la funcion de desencriptarlo y guardar la imagen.