import boto3

bucket_name = "mi-bucket-udc-2026-002"

s3 = boto3.client("s3")

try:
    s3.delete_bucket(Bucket=bucket_name)
    print(f"✅ Bucket eliminado: {bucket_name}")

except Exception as e:
    print("❌ Error al eliminar el bucket:")
    print(e)