from django.db import models
import random
import string
from django.conf import settings


class Shortener(models.Model) :
    original_url = models.URLField(max_length=200)
    hash = models.URLField(blank=True, null=True,max_length=10)
    creation_date = models.DateTimeField(auto_now_add=True)

    def shortener(self) :
        while True :
            char = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(7))
            new_link = settings.HOST_URL+'/'+ char
            if not Shortener.objects.filter(hash = new_link).exists() :
                break
        return new_link

    def save(self, *args, **kwargs) :
        if not self.hash :
            new_link = self.shortener()
            self.hash = new_link
        return super().save(*args, **kwargs)

