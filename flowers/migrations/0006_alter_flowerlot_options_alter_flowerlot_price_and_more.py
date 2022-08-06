# Generated by Django 4.1 on 2022-08-06 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0005_rename_amount_flowerlot_quantity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flowerlot',
            options={'verbose_name': 'Экземпляр лота', 'verbose_name_plural': 'Экземпляры лот'},
        ),
        migrations.AlterField(
            model_name='flowerlot',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('Seller', 'Seller'), ('Buyer', 'Buyer')], max_length=10),
        ),
    ]
