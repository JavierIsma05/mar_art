from django.db import models
from django.urls import reverse


class ServicePlan(models.Model):
    """Modelo para planes de servicios"""
    
    STATUS_CHOICES = [
        ('active', 'Activo'),
        ('inactive', 'Inactivo'),
    ]
    
    name = models.CharField(max_length=200, verbose_name='Nombre del plan')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Slug')
    description = models.TextField(verbose_name='Descripción')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    includes = models.TextField(help_text='Separar cada característica con una coma', verbose_name='Incluye')
    is_featured = models.BooleanField(default=False, verbose_name='Destacado')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active', verbose_name='Estado')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado el')
    
    class Meta:
        ordering = ['-is_featured', 'price']
        verbose_name = 'Plan de servicio'
        verbose_name_plural = 'Planes de servicios'
    
    def __str__(self):
        return self.name
    
    def get_includes_list(self):
        """Retorna la lista de características incluidas"""
        return [item.strip() for item in self.includes.split(',') if item.strip()]
    
    def get_absolute_url(self):
        return reverse('services')
