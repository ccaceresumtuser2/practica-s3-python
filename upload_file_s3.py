import boto3
from botocore.exceptions import NoCredentialsError

# Crear cliente S3
s3 = boto3.client(
    's3')
archivo_local = 'C:/s3app/file/upload/certificado.pdf'
bucket = 'mi-bucket-udc-2026-001'
ruta_en_s3 = 'documentos/certificacion.pdf'  # Ruta dentro del bucket

try:
    s3.upload_file(archivo_local, bucket, ruta_en_s3)
    print("Archivo subido correctamente")
except FileNotFoundError:
    print("El archivo no existe")
except NoCredentialsError:
    print("Credenciales incorrectas")