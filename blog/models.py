from django.db import models
from django.urls import reverse


class BlogPost(models.Model):
    """Modelo para posts del blog"""
    
    STATUS_CHOICES = [
        ('draft', 'Borrador'),
        ('published', 'Publicado'),
    ]
    
    CATEGORY_CHOICES = [
        ('tips', 'Consejos'),
        ('news', 'Novedades'),
        ('tutorial', 'Tutorial'),
        ('inspiration', 'Inspiración'),
        ('other', 'Otro'),
    ]
    
    title = models.CharField(max_length=200, verbose_name='Título')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Slug')
    summary = models.TextField(max_length=300, verbose_name='Resumen')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(upload_to='blog/', verbose_name='Imagen')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name='Categoría')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft', verbose_name='Estado')
    publication_date = models.DateField(verbose_name='Fecha de publicación')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado el')
    
    class Meta:
        ordering = ['-publication_date']
        verbose_name = 'Post del blog'
        verbose_name_plural = 'Posts del blog'
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})
