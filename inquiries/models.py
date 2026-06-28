from django.db import models


class Inquiry(models.Model):
    """Solicitud de cotizacion para productos personalizados."""

    STATUS_CHOICES = [
        ('new', 'Pendiente'),
        ('contacted', 'Revisada'),
        ('closed', 'Completada'),
        ('cancelled', 'Cancelada'),
    ]

    SERVICE_CHOICES = [
        ('camisetas', 'Camisetas'),
        ('hoodies', 'Hoodies'),
        ('stickers', 'Stickers'),
        ('tarjetas', 'Tarjetas'),
        ('tazas', 'Tazas'),
        ('encendedores', 'Encendedores'),
        ('bolsos', 'Bolsos'),
        ('negocios', 'Productos para negocios'),
        ('otros', 'Otros personalizados'),
    ]

    full_name = models.CharField(max_length=200, verbose_name='Nombre completo')
    whatsapp = models.CharField(max_length=20, verbose_name='WhatsApp')
    email = models.EmailField(blank=True, verbose_name='Email')
    service_interest = models.CharField(max_length=30, choices=SERVICE_CHOICES, verbose_name='Tipo de producto')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Cantidad')
    needed_date = models.DateField(null=True, blank=True, verbose_name='Fecha requerida')
    message = models.TextField(verbose_name='Descripcion de la idea')
    reference_image = models.ImageField(upload_to='inquiries/references/', blank=True, verbose_name='Imagen de referencia')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name='Estado')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Solicitud de cotizacion'
        verbose_name_plural = 'Solicitudes de cotizacion'

    def __str__(self):
        return f"{self.full_name} - {self.service_interest}"
