import boto3
import os
from concurrent.futures import ThreadPoolExecutor

bucket_name = "mi-bucket-udc-2026-002"
#carpeta_local = "./file/upload"  # Cambia esta ruta a tu carpeta local
carpeta_local = 'C:/s3app/file/upload'  # Cambia esta ruta a tu carpeta local

s3 = boto3.client("s3")

def subir_archivo(archivo):
    ruta = os.path.join(carpeta_local, archivo)
    
    try:
        s3.upload_file(
            ruta,
            bucket_name,
            archivo,
            ExtraArgs={"ACL": "public-read"}
        )
        print(f"✅ Subido: {archivo}")
    except Exception as e:
        print(f"❌ Error con {archivo}: {e}")


archivos = []
#os.listdir() devuelve todo lo que hay dentro de la carpeta.
for f in os.listdir(carpeta_local):
    #construye ruta de archivo completa
    ruta = os.path.join(carpeta_local, f)
    #Verificar que sea un archivo
    if os.path.isfile(ruta):
        #Agregar el archivo a la lista
        archivos.append(f)
'''
Esto crea 10 hilos (threads) para ejecutar tareas al mismo tiempo.
Piensa en esto como 10 trabajadores subiendo archivos al mismo tiempo.
'''
with ThreadPoolExecutor(max_workers=10) as executor:
    '''
    Ejecutar la función en paralelo
    esto hace
    subir_archivo("doc1.pdf")
    subir_archivo("doc2.txt")
    subir_archivo("notas.docx")
    '''
    '''ejecuta el hilo por map
    Thread1 → doc1.pdf
    Thread2 → doc2.txt
    Thread3 → notas.docx'''
    executor.map(subir_archivo, archivos)