import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_project_is_featured_project_tags_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectgallery',
            options={'verbose_name': 'Imagen de galeria', 'verbose_name_plural': 'Imagenes de galeria'},
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='project',
            name='publication_date',
            field=models.DateField(verbose_name='Fecha de publicacion'),
        ),
        migrations.AlterField(
            model_name='projectgallery',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='portfolio.project', verbose_name='Trabajo'),
        ),
    ]
