# Generated by Django 4.1.4 on 2022-12-26 20:35

from django.db import migrations, models
import treasuremap.fields


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0003_post_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='lonlatstr',
            field=models.CharField(blank=True, max_length=255, verbose_name='Для запроса'),
        ),
        migrations.AlterField(
            model_name='post',
            name='point',
            field=treasuremap.fields.LatLongField(max_length=24),
        ),
    ]
