from django.db import models
from django.contrib.auth.models import User

class ActivationCode(models.Model):
    code = models.CharField(max_length=32)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @classmethod
    def create(cls, user, code):
        activationCode = cls(code=code, user=user)
        return activationCode
