# Generated by Django 4.2.2 on 2023-06-22 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_company_card_icon_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='card_background_color',
            field=models.CharField(default='#ffffff', max_length=20),
        ),
    ]
