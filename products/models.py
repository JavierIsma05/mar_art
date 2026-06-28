from django.db import models
from django.urls import reverse


class Product(models.Model):
    """Catalogo de productos personalizados."""

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
        ('otros', 'Otros personalizados'),
    ]

    title = models.CharField(max_length=200, verbose_name='Titulo')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Slug')
    description = models.TextField(verbose_name='Descripcion')
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, verbose_name='Categoria')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Precio base')
    main_image = models.ImageField(upload_to='products/main/', verbose_name='Imagen principal')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft', verbose_name='Estado')
    is_available = models.BooleanField(default=True, verbose_name='Disponible')
    is_featured = models.BooleanField(default=False, verbose_name='Producto destacado')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado el')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    @property
    def quote_url(self):
        return f"{reverse('contact')}?producto={self.slug}"


class ProductGallery(models.Model):
    """Galeria de imagenes para productos."""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='gallery', verbose_name='Producto')
    image = models.ImageField(upload_to='products/gallery/', verbose_name='Imagen')
    caption = models.CharField(max_length=200, blank=True, verbose_name='Pie de foto')

    class Meta:
        verbose_name = 'Imagen de galeria'
        verbose_name_plural = 'Imagenes de galeria'

    def __str__(self):
        return f"{self.product.title} - {self.caption or 'Sin caption'}"
