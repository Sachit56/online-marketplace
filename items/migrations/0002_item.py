# Generated by Django 5.0 on 2023-12-09 10:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('price', models.IntegerField()),
                ('is_sold', models.BooleanField(default=False)),
                ('created_at', models.DateField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='item_images')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
