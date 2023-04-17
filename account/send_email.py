from django.core.mail import send_mail
from decouple import config

def send_activation_code(email, code):
    send_mail(
        'MovAPI',
        f'http://localhost:8000/account/activate/{code}/', #body
        'szhokee@gmail.com', #from
        [email]   # to
    )

def send_reset_password_code(email, code):
    send_mail(
        'MovAPI',
        f'To reset your password use this code {code}',
        config('EMAIL_HOST_USER'),
        [email]
    )
