import boto3

bucket_name = "mi-bucket-udc-2026-002"

s3 = boto3.resource("s3")
bucket = s3.Bucket(bucket_name)

try:
    bucket.objects.all().delete()
    print("✅ Todos los archivos fueron eliminados")

except Exception as e:
    print("❌ Error al eliminar archivos")
    print(e)