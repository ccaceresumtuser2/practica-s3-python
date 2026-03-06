import boto3
import os

bucket_name = "mi-bucket-udc-2026-002"
carpeta_local = "C:/s3app/file/upload"

s3 = boto3.client("s3")

# extensiones permitidas
extensiones = (".pdf", ".doc", ".docx", ".txt")

try:
    for archivo in os.listdir(carpeta_local):

        ruta_archivo = os.path.join(carpeta_local, archivo)

        if os.path.isfile(ruta_archivo) and archivo.lower().endswith(extensiones):

            key_s3 = f"documento/{archivo}"

            s3.upload_file(ruta_archivo, bucket_name, key_s3)

            print(f"✅ Subido: {key_s3}")

except Exception as e:
    print("❌ Error al subir archivos:")
    print(e)