# Generated by Django 3.1 on 2021-04-03 19:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portfolio', '0003_auto_20210115_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='activity',
            field=models.URLField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(default='', upload_to='Portfolios/'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='languages',
            field=models.URLField(default='', null=True),
        ),
    ]