from django.core.mail import send_mail
from .models import ActivationCode
import hashlib, time

def SendActivationLink(user):
    activationCode = GenerateActivationCode(user)
    acObject = ActivationCode.create(user, activationCode)
    acObject.save()
    # send an email
    message = 'Your activation link: ' + 'http://127.0.0.1:8000/user-manager/activate/' + str(activationCode)
    # with mail.get_connection(fail_silently=False) as connection:
    send_mail(
    'Activate your account',
    message,
    'from@example.com',
    ['moj_email@example.com'],
    fail_silently=False)

    return

def GenerateActivationCode(user):
    hasher = hashlib.sha256()
    seed = str(user.id) + str(time.time())
    hasher.update(bytes(seed, 'ascii'))
    activationCode = str(hasher.digest().hex())
    return activationCode