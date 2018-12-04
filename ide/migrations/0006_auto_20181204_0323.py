# Generated by Django 2.1.4 on 2018-12-04 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ide', '0005_auto_20181204_0320'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeFuzzy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='co-norm')),
            ],
        ),
        migrations.AlterField(
            model_name='system',
            name='conorm',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ide.CONorm'),
        ),
        migrations.AlterField(
            model_name='system',
            name='tnorm',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ide.TNorm'),
        ),
    ]