from django.db import models
from django.utils.text import slugify

class Ad(models.Model):
    title = models.CharField(max_length=127)
    description = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    slug = models.SlugField(max_length=150, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        creating = self.pk is None
        super().save(*args, **kwargs)

        if creating and not self.slug:
            self.slug = f"{slugify(self.title)}-{self.pk}"
            super().save(update_fields=["slug"])

    def __str__(self):
        return f"{self.pk}. {self.title}"
