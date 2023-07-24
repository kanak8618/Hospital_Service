# Generated by Django 4.2.3 on 2023-07-20 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_service_oxygen_cylinder_available'),
    ]

    operations = [
        migrations.CreateModel(
            name='facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='', max_length=60)),
            ],
        ),
        migrations.DeleteModel(
            name='service',
        ),
    ]
