# Generated by Django 2.1.4 on 2018-12-04 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ide', '0003_auto_20181204_0247'),
    ]

    operations = [
        migrations.AddField(
            model_name='functioncategory',
            name='params',
            field=models.CharField(default='', max_length=1024, verbose_name='Params'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='function',
            name='a',
            field=models.FloatField(blank=True, null=True, verbose_name='a'),
        ),
        migrations.AlterField(
            model_name='function',
            name='b',
            field=models.FloatField(blank=True, null=True, verbose_name='b'),
        ),
        migrations.AlterField(
            model_name='function',
            name='c',
            field=models.FloatField(blank=True, null=True, verbose_name='c'),
        ),
        migrations.AlterField(
            model_name='function',
            name='d',
            field=models.FloatField(blank=True, null=True, verbose_name='d'),
        ),
    ]