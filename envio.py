"""
Este script envía correos desde gmail con mi correo personal
el correo se envía en formato HTML para una mejor presentación,
todo debe estar en la misma carpeta
"""
import smtplib, ssl
import os
#################################################################################
#estas librerias son para adjuntar texto y HTML
#################################################################################
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#################################################################################
#estas librerias son para adjuntar imágenes
#################################################################################
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path
#################################################################################
#################################################################################
class Mail:
 def __init__(self):
  #################################################################################
  #Inicio del servicio SMTP con los datos del correo que envía
  #################################################################################
  self.port=465
  self.smtp_server_domain_name="smtp.gmail.com"
  self.sender_mail="osvamail02@gmail.com"
  self.password=os.environ.get("CLAVEGMAIL")

 def send(self,emails):
  #################################################################################
  #Inicio del servicio SMTP
  #################################################################################
  ssl_context=ssl.create_default_context()
  service=smtplib.SMTP_SSL(self.smtp_server_domain_name,self.port,context=ssl_context)
  service.login(self.sender_mail,self.password)
  #################################################################################
  #Apertura de los archivos de texto y html que se van a enviar
  #################################################################################
  with open("saludo.txt","r") as lectura:
   text_template=lectura.read()
  with open("contenidoHTML.html","r") as archivo:
   html_template=archivo.read()
  file_path="hojadeVidaOscarFernandoValencia.pdf"
  foto=MIMEBase("application", "octet-stream")
  with open(file_path, "rb") as file:
   foto.set_payload(file.read())
  encoders.encode_base64(foto)
  foto.add_header("Content-Disposition", f"attachment; filename={Path(file_path).name}")
  #################################################################################
  #################################################################################
  #Lectura de los datos y envío del correo:
  #################################################################################

  for email in emails:
   mail=MIMEMultipart('alternative')
   mail['Subject']='Hoja de vida Oscar Valencia'
   mail['From']=self.sender_mail
   mail['To']=email
   #################################################################################
   #Se debe dar el formato correcto a los archivos antes de adjuntarlos
   #################################################################################
   html_content = MIMEText(html_template,'html')
   text_content = MIMEText(text_template,'plain')
   encoders.encode_base64(foto)
   foto.add_header("Content-Disposition", f"attachment; filename={Path(file_path).name}")
   #################################################################################
   #Se adjuntan los archivos leídos anteriormente
   #################################################################################
   mail.attach(text_content)
   mail.attach(html_content)
   mail.attach(foto)
   #################################################################################
   #Enviando el correo:
   #################################################################################
   result=service.sendmail(self.sender_mail,email,mail.as_string())
   print("Se envió el correo a",email)
  #################################################################################
  #Fin del envio de correos y cierre del servicio SMTP
  #################################################################################
  service.quit()
#################################################################################
#################################################################################
 #Creación del objeto Mail:
#################################################################################
if __name__=='__main__':
 #################################################################################
 #Cargando el archivo que tiene los correos
 #################################################################################
 with open("remitentes.txt","r") as correos:
  mails=correos.readlines() 
 #################################################################################
 #Creación del objeto Mail:
 #################################################################################
 mail=Mail()
 #################################################################################
 #iniciando la carga de datos y envío del correo
 #################################################################################
 mail.send(mails)
