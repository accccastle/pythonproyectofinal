from django.db import models

class Brand(models.Model):
    TYPE_CHOICES = (
    ('Mercado','Mercado'),
    ('Restaurante','Restaurante'),
    ('Emprendimiento','Emprendimiento'),
    )
    
    name = models.CharField(max_length=50, unique=True)
    type_brand = models.CharField(max_length=50, choices = TYPE_CHOICES)
    web = models.URLField(max_length=200)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='brand_pictures', null=True, blank=True)
    
    def __str__(self):
        return f'{self.name} - {self.image}'

    
    
    
    
