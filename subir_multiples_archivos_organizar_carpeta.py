import boto3
import os

bucket_name = "mi-bucket-udc-2026-002"
carpeta_local = "C:/s3app/file/upload"

s3 = boto3.client("s3")

try:

    for archivo in os.listdir(carpeta_local):

        ruta_archivo = os.path.join(carpeta_local, archivo)

        if os.path.isfile(ruta_archivo):

            extension = archivo.lower().split(".")[-1]

            # definir carpeta según tipo
            if extension == "pdf":
                carpeta_s3 = "pdf"
            elif extension in ["doc", "docx"]:
                carpeta_s3 = "word"
            elif extension == "txt":
                carpeta_s3 = "txt"
            else:
                continue  # ignorar otros tipos

            key_s3 = f"documentos/{carpeta_s3}/{archivo}"

            s3.upload_file(ruta_archivo, bucket_name, key_s3)

            print(f"✅ Subido: {key_s3}")

except Exception as e:
    print("❌ Error al subir archivos:")
    print(e)