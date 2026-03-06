import boto3

bucket_name = "mi-bucket-udc-2026-001"
s3_key = 'documentos1/Prueba2.pdf'   # <-- ruta exacta dentro del bucket
local_file = 'C:/s3app/file/download/Prueba1.pdf'        # <-- nombre en tu máquina
s3 = boto3.client("s3")
s3.download_file(bucket_name, s3_key, local_file)
print("Archivo descargado correctamente.")