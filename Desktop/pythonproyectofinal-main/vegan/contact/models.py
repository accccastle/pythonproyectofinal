from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    email = models.EmailField(verbose_name='Correo Electrónico')
    message = models.TextField(verbose_name='Mensaje')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
        ordering = ['-created']

    def __str__(self):
        return self.name
