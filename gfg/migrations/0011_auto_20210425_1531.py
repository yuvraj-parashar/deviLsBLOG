# Generated by Django 3.1.5 on 2021-04-25 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gfg', '0010_auto_20210425_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaderboard',
            name='daily_question',
        ),
        migrations.AlterField(
            model_name='leaderboard',
            name='weekly_score',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
