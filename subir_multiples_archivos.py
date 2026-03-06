import boto3
import os

bucket_name = "mi-bucket-udc-2026-002"
#carpeta_local = "./file/upload"  # Cambia esta ruta a tu carpeta local
carpeta_local = 'C:/s3app/file/upload'  # Cambia esta ruta a tu carpeta local
s3 = boto3.client("s3")

try:
    for archivo in os.listdir(carpeta_local):
        ruta_archivo = os.path.join(carpeta_local, archivo)

        if os.path.isfile(ruta_archivo):
            s3.upload_file(ruta_archivo, bucket_name, "documento/"+archivo)
            print(f"✅ Subido: {archivo}")

except Exception as e:
    print("❌ Error al subir archivos:")
    print(e)