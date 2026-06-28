from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_featured',
            field=models.BooleanField(default=False, verbose_name='Trabajo destacado'),
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.CharField(blank=True, max_length=250, verbose_name='Etiquetas'),
        ),
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('camisetas', 'Camisetas'), ('hoodies', 'Hoodies'), ('stickers', 'Stickers'), ('tarjetas', 'Tarjetas'), ('tazas', 'Tazas'), ('encendedores', 'Encendedores'), ('bolsos', 'Bolsos'), ('negocios', 'Productos para negocios'), ('eventos', 'Eventos'), ('otros', 'Otros personalizados')], max_length=30, verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='project',
            name='client_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Cliente o tipo de cliente'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Titulo'),
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-publication_date'], 'verbose_name': 'Trabajo reciente', 'verbose_name_plural': 'Trabajos recientes'},
        ),
    ]
