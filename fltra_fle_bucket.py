import boto3

try:
    bucket_name = "mi-bucket-udc-2026-002"
    s3 = boto3.client("s3")
    paginator = s3.get_paginator("list_objects_v2")

    #extensiones = (".pdf", ".doc", ".docx", ".txt")
    extensiones = (".pdf", ".docx", "txt")
    for page in paginator.paginate(Bucket=bucket_name):
        if "Contents" in page:
            for obj in page["Contents"]:
                key = obj["Key"].lower()

                if key.endswith(extensiones):
                    print(f"Archivo: {obj['Key']}")
                    print(f"  Tamaño: {obj['Size']} bytes")
                    print(f"  Última modificación: {obj['LastModified']}")
                    print("-" * 40)

except Exception as e:
    print("❌ Error inesperado:")
    print(e)