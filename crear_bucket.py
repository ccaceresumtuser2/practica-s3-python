import boto3
from botocore.exceptions import ClientError

bucket_name = "mi-bucket-udc-2026-002"
region = "us-east-1"

s3 = boto3.client("s3", region_name=region)

def bucket_exists(name):
    try:
        s3.head_bucket(Bucket=name)
        return True
    except ClientError:
        return False

if bucket_exists(bucket_name):
    print("ℹ️ El bucket ya existe.")
else:
    try:
        if region == "us-east-1":
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={
                    "LocationConstraint": region
                }
            )
        print("✅ Bucket creado correctamente.")
    except ClientError as e:
        print("❌ Error al crear el bucket:")
        print(e)