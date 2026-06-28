from django.db import models
from django.urls import reverse


class Project(models.Model):
    """Trabajos recientes y publicaciones visuales del emprendimiento."""

    STATUS_CHOICES = [
        ('draft', 'Borrador'),
        ('published', 'Publicado'),
        ('featured', 'Destacado'),
    ]

    CATEGORY_CHOICES = [
        ('camisetas', 'Camisetas'),
        ('hoodies', 'Hoodies'),
        ('stickers', 'Stickers'),
        ('tarjetas', 'Tarjetas'),
        ('tazas', 'Tazas'),
        ('encendedores', 'Encendedores'),
        ('bolsos', 'Bolsos'),
        ('negocios', 'Productos para negocios'),
        ('eventos', 'Eventos'),
        ('otros', 'Otros personalizados'),
    ]

    title = models.CharField(max_length=200, verbose_name='Titulo')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Slug')
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, verbose_name='Categoria')
    description = models.TextField(verbose_name='Descripcion')
    main_image = models.ImageField(upload_to='portfolio/main/', verbose_name='Imagen principal')
    client_name = models.CharField(max_length=200, blank=True, verbose_name='Cliente o tipo de cliente')
    tags = models.CharField(max_length=250, blank=True, verbose_name='Etiquetas')
    is_featured = models.BooleanField(default=False, verbose_name='Trabajo destacado')
    publication_date = models.DateField(verbose_name='Fecha de publicacion')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft', verbose_name='Estado')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado el')

    class Meta:
        ordering = ['-publication_date']
        verbose_name = 'Trabajo reciente'
        verbose_name_plural = 'Trabajos recientes'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})


class ProjectGallery(models.Model):
    """Galeria de imagenes para trabajos recientes."""

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='gallery', verbose_name='Trabajo')
    image = models.ImageField(upload_to='portfolio/gallery/', verbose_name='Imagen')
    caption = models.CharField(max_length=200, blank=True, verbose_name='Pie de foto')

    class Meta:
        verbose_name = 'Imagen de galeria'
        verbose_name_plural = 'Imagenes de galeria'

    def __str__(self):
        return f"{self.project.title} - {self.caption or 'Sin caption'}"
