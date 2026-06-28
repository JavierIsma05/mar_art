from django.db import models


class Testimonial(models.Model):
    """Modelo para testimonios de clientes"""
    
    name = models.CharField(max_length=200, verbose_name='Nombre')
    role = models.CharField(max_length=200, verbose_name='Rol/Cargo')
    message = models.TextField(verbose_name='Mensaje')
    image = models.ImageField(upload_to='testimonials/', blank=True, verbose_name='Imagen')
    is_active = models.BooleanField(default=True, verbose_name='Activo')
    
    class Meta:
        verbose_name = 'Testimonio'
        verbose_name_plural = 'Testimonios'
    
    def __str__(self):
        return f"{self.name} - {self.role}"


class SiteConfiguration(models.Model):
    """Modelo para configuración general del sitio"""
    
    brand_name = models.CharField(max_length=200, verbose_name='Nombre de la marca')
    slogan = models.CharField(max_length=300, verbose_name='Eslogan')
    whatsapp = models.CharField(max_length=20, verbose_name='WhatsApp')
    instagram = models.CharField(max_length=200, blank=True, verbose_name='Instagram')
    email = models.EmailField(verbose_name='Email')
    logo = models.ImageField(upload_to='site/', blank=True, verbose_name='Logo')
    primary_color = models.CharField(max_length=7, default='#2563EB', verbose_name='Color primario')
    secondary_color = models.CharField(max_length=7, default='#7C3AED', verbose_name='Color secundario')
    
    class Meta:
        verbose_name = 'Configuración del sitio'
        verbose_name_plural = 'Configuraciones del sitio'
    
    def __str__(self):
        return self.brand_name


class SiteBanner(models.Model):
    """Banner administrable para promociones del inicio."""

    title = models.CharField(max_length=180, verbose_name='Titulo')
    subtitle = models.CharField(max_length=260, blank=True, verbose_name='Subtitulo')
    image = models.ImageField(upload_to='site/banners/', blank=True, verbose_name='Imagen')
    button_text = models.CharField(max_length=80, blank=True, verbose_name='Texto del boton')
    button_url = models.CharField(max_length=220, blank=True, verbose_name='URL del boton')
    is_active = models.BooleanField(default=True, verbose_name='Activo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Banner del inicio'
        verbose_name_plural = 'Banners del inicio'

    def __str__(self):
        return self.title
