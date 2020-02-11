from email.mime.text import MIMEText
import smtplib

def send_email(email,name):
    to_email = email
    subject = "Confirmation Message"
    message = """<h3>Thankyou for contacting me. I will get back to you as soon as possible </h3><br><h5>Regards<br>Bhoomika Garg</h5>"""
    msg = MIMEText(message,'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail = smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)
