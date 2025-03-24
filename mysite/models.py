from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class UserType(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        app_label = 'mysite'
        verbose_name = 'Kullanıcı Tipi'
        verbose_name_plural = 'Kullanıcı Tipleri'

    def __str__(self):
        return self.name


class UserRole(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        app_label = 'mysite'
        verbose_name = 'Kullanıcı Rolü'
        verbose_name_plural = 'Kullanıcı Rolleri'

    def __str__(self):
        return self.name


