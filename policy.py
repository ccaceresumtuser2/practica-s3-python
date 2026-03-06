import boto3
import json
from botocore.exceptions import ClientError

bucket_name = "mi-bucket-udc-2026-002"

s3 = boto3.client("s3")

try:

    # leer archivo json
    with open("policy.json", "r") as file:
        policy = json.load(file)

    # aplicar policy al bucket
    s3.put_bucket_policy(
        Bucket=bucket_name,
        Policy=json.dumps(policy)
    )

    print(f"✅ Política aplicada al bucket {bucket_name}")

except ClientError as e:
    print("❌ Error al aplicar la política:")
    print(e)