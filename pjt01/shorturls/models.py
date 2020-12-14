from django.db import models
from django.core.validators import URLValidator

# Create your models here.

class OptionalSchemeURLValidator(URLValidator):
    def __call__(self, value):
        # if input url has no http:// or https://
        if '://' not in value:
            value = 'http://' + value
        super(OptionalSchemeURLValidator, self).__call__(value)


class History(models.Model):
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Urls(models.Model):
    # original url (not URLField)
    original = models.TextField(blank=True, null=True, validators=[OptionalSchemeURLValidator()])
    edit = models.TextField()
    # encoded result from index
    encoding = models.CharField(max_length=8)

    def __str__(self):
        return self.original