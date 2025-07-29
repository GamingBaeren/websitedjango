from django.core.mail import send_mail
from django.conf import settings

def send_test_email():
    subject = 'Test Email from Django'
    message = 'This is a test email to verify SMTP configuration.'
    from_email = settings.EMAIL_HOST_USER  # Use the SMTP user as sender
    recipient_list = [settings.EMAIL_HOST_USER]  # Send to the same email for testing

    send_mail(subject, message, from_email, recipient_list)
