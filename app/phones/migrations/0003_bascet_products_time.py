# Generated by Django 4.1.5 on 2023-03-22 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_alter_airpods_comments_rate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bascet_products',
            name='time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
