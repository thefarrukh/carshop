from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class MediaFile(BaseModel):
    file = models.FileField(upload_to='files/')
    car = models.ForeignKey(
        'cars.Car',
        on_delete=models.CASCADE,
        related_name='media_files',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.file.name
