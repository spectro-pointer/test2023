import os
import ftplib

# Dirección del servidor FTP
server = "web20.swisscenter.com"

# Nombre de usuario y contraseña para iniciar sesión en el servidor
username = "akc001_datos1_espectrales"
password = "wmlTHuBvYF.umc7"

# Nombre de la carpeta que se va a subir
folder = "C:/Users/Sophie/Documents/Gustavo/Documents/ESPETROSCOPIA/Copia_spectrometro_python2/spectrometer2"

# Abrir una conexión FTP con el servidor
ftp = ftplib.FTP(server)

# Iniciar sesión en el servidor
ftp.login(username, password)

# Crear una función para subir un archivo a la carpeta actual del servidor FTP
def upload_file(ftp, file):
    with open(file, "rb") as f:
        ftp.storbinary("STOR " + file, f)

# Crear una función para subir una carpeta y todos sus archivos y carpetas a la carpeta actual del servidor FTP
def upload_folder(ftp, folder):
    for root, dirs, files in os.walk(folder):
        for dir in dirs:
            ftp.mkd(dir)
            ftp.cwd(dir)
            upload_folder(ftp, dir)
            ftp.cwd("..")
        for file in files:
            upload_file(ftp, file)

# Subir la carpeta y todos sus archivos y carpetas a la carpeta actual del servidor FTP
upload_folder(ftp, folder)

# Cerrar la conexión FTP con el servidor
ftp.quit()
