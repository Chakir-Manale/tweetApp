from django.conf import settings
from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.

def validate_content(value):
    content = value
    if content == "":
        raise ValidationError("Cpntent cannot be empty!")
    return value


class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=140, validators=[validate_content])
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + "." + str(self.content)

    """
    def clean(self, *args, **kwargs):
        content = self.content
        if content == "":
            raise ValidationError("Cpntent cannot be empty!")
        return super(Tweet, self).clean(*args, **kwargs)
    """