import smtplib
import ssl
from email.message import EmailMessage
import os
from gtts import gTTS
from playsound import playsound


#Importando la clave del correo
clave=os.environ.get("CLAVE_GMAIL")
# Define email sender and receiver
email_sender="osvamail02@gmail.com"
email_password=clave
#Se deben agregar todos los destinatarios a esta lista:
email_receiver=["practicante2dtcordoba@gmail.com","osvamail02@gmail.com","osvalen@zoho.com","ofernando.valencia@udea.edu.co","asesoriaseuler@zoho.com"]

# Set the subject and body of the email
subject='Check out my new video!'
#El archivo a mandar debe estar en la misma carpeta del script
with open("ensayoCorreo.txt","r",encoding="utf-8") as archivo:
 body=archivo.read()

em=EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['Subject']=subject
em.set_content(body)

# Add SSL (layer of security)
context=ssl.create_default_context()

# Log in and send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
 smtp.login(email_sender, email_password)
 smtp.sendmail(email_sender,email_receiver,em.as_string())

#Avisar que ya se realizó el proceso:
linea="Se han enviado los correos masivos con python"
leer=gTTS(text=linea,lang="es")
leer.save("/tmp/leeme.mp3")
playsound("/tmp/leeme.mp3")

