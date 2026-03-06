import boto3

bucket_name = "mi-bucket-udc-2026-002"
archivo = "ACUERDO No. 03 - CALENDARIO DE INSCRIPCIONES 2026-2.pdf"

s3 = boto3.client("s3")

try:
    s3.delete_object(
        Bucket=bucket_name,
        Key=archivo
    )

    print(f"✅ Archivo eliminado: {archivo}")

except Exception as e:
    print("❌ Error al eliminar archivo")
    print(e)