from django.db import models


class CalendarTask(models.Model):
    """Trabajo interno agendado por el admin para entregas o recordatorios."""

    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('in_progress', 'En proceso'),
        ('done', 'Entregado'),
        ('cancelled', 'Cancelado'),
    ]

    PRIORITY_CHOICES = [
        ('normal', 'Normal'),
        ('high', 'Alta'),
        ('urgent', 'Urgente'),
    ]

    title = models.CharField(max_length=200, verbose_name='Trabajo o recordatorio')
    client_name = models.CharField(max_length=200, blank=True, verbose_name='Cliente')
    due_date = models.DateField(verbose_name='Fecha de entrega')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='normal', verbose_name='Prioridad')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='Estado')
    notes = models.TextField(blank=True, verbose_name='Notas')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado el')

    class Meta:
        ordering = ['due_date', 'title']
        verbose_name = 'Trabajo agendado'
        verbose_name_plural = 'Trabajos agendados'

    def __str__(self):
        return self.title
