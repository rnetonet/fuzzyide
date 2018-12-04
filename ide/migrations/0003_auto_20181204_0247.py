# Generated by Django 2.1.4 on 2018-12-04 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ide', '0002_auto_20181204_0155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('a', models.FloatField(null=True, verbose_name='a')),
                ('b', models.FloatField(null=True, verbose_name='b')),
                ('c', models.FloatField(null=True, verbose_name='c')),
                ('d', models.FloatField(null=True, verbose_name='d')),
            ],
        ),
        migrations.CreateModel(
            name='FunctionCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
        ),
        migrations.AddField(
            model_name='function',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ide.FunctionCategory'),
        ),
        migrations.AddField(
            model_name='function',
            name='system',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ide.System'),
        ),
    ]