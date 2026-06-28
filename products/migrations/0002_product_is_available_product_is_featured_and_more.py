from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_available',
            field=models.BooleanField(default=True, verbose_name='Disponible'),
        ),
        migrations.AddField(
            model_name='product',
            name='is_featured',
            field=models.BooleanField(default=False, verbose_name='Producto destacado'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('camisetas', 'Camisetas'), ('hoodies', 'Hoodies'), ('stickers', 'Stickers'), ('tarjetas', 'Tarjetas'), ('tazas', 'Tazas'), ('encendedores', 'Encendedores'), ('bolsos', 'Bolsos'), ('negocios', 'Productos para negocios'), ('otros', 'Otros personalizados')], max_length=30, verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Precio base'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Titulo'),
        ),
    ]
