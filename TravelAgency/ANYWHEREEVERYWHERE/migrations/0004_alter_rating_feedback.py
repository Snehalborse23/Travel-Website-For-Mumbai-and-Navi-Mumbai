# Generated by Django 4.1.7 on 2023-04-23 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ANYWHEREEVERYWHERE', '0003_alter_rating_feedback_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='feedback',
            field=models.TextField(default='No feedback given'),
        ),
    ]