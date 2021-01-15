# Generated by Django 3.1.1 on 2021-01-15 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(default='', upload_to='projects/'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='trends',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default=None, max_length=128),
            preserve_default=False,
        ),
    ]
