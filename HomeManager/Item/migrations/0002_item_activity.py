# Generated by Django 4.0.5 on 2022-06-16 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Item', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='activity',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Item.activity'),
        ),
    ]
