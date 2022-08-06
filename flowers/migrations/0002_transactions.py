# Generated by Django 4.0.6 on 2022-07-31 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('flowers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='buyers', to=settings.AUTH_USER_MODEL)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('lot', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='lots', to='flowers.flowerlot')),
                ('salesman', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='salesmans', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
