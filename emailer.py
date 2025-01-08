import smtplib
from email.message import EmailMessage

# Define email content
email_sender = "youremail@email.com"
email_sender_password = "yourpassword"
email_receiver = "theiremail@email.com"

# Create the email message
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = "My first Python Email"
em.set_content("What up dude.")

# Set up the SMTP server and send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:  # Use SMTP_SSL for port 465
    smtp.login(email_sender, email_sender_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
