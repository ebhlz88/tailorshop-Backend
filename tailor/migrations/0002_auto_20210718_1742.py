# Generated by Django 3.2 on 2021-07-18 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tailor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='measurementFK',
        ),
        migrations.AddField(
            model_name='measurements',
            name='cutomerFK',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='tailor.customer'),
            preserve_default=False,
        ),
    ]
