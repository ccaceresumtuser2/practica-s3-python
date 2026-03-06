Practica-s3-python

Instalar AWS CLI

https://awscli.amazonaws.com/AWSCLIV2.msi
Lo prueban en la Consola, CMD o PowerShell y ejecuta:
aws --version

###Instalar la libreria boto3
pip install boto3

En windows configura las credenciales con El laboratorio Lab 3.1: Working with Amazon S3 del Curso

Creas la carpeta .aws en tu carpeta User
C:\Users\TU_USUARIO\.aws\
.aws

├── credentials
 
 └── config

 Archivo config
 [default]
 region = us-east-1
 output = json

 Archivo credentials
 El archivo credential se copia AWS CLI, que se encuentra en el laboratorio  details->show->Credentials
 Copy and paste the following into ~/.aws/credentials
