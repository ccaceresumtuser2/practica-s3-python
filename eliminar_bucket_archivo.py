import boto3

bucket_name = "mi-bucket-udc-2026-002"

s3 = boto3.resource("s3")
bucket = s3.Bucket(bucket_name)

try:
    
    # eliminar todos los objetos
    bucket.objects.all().delete()
    
    # eliminar bucket
    bucket.delete()

    print(f"✅ Bucket eliminado completamente: {bucket_name}")

except Exception as e:
    print("❌ Error:")
    print(e)