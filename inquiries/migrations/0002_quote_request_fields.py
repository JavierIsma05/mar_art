from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquiries', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inquiry',
            options={'ordering': ['-created_at'], 'verbose_name': 'Solicitud de cotizacion', 'verbose_name_plural': 'Solicitudes de cotizacion'},
        ),
        migrations.AddField(
            model_name='inquiry',
            name='needed_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha requerida'),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='Cantidad'),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='reference_image',
            field=models.ImageField(blank=True, upload_to='inquiries/references/', verbose_name='Imagen de referencia'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='message',
            field=models.TextField(verbose_name='Descripcion de la idea'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='service_interest',
            field=models.CharField(choices=[('camisetas', 'Camisetas'), ('hoodies', 'Hoodies'), ('stickers', 'Stickers'), ('tarjetas', 'Tarjetas'), ('tazas', 'Tazas'), ('encendedores', 'Encendedores'), ('bolsos', 'Bolsos'), ('negocios', 'Productos para negocios'), ('otros', 'Otros personalizados')], max_length=30, verbose_name='Tipo de producto'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='status',
            field=models.CharField(choices=[('new', 'Pendiente'), ('contacted', 'Revisada'), ('closed', 'Completada'), ('cancelled', 'Cancelada')], default='new', max_length=20, verbose_name='Estado'),
        ),
    ]
