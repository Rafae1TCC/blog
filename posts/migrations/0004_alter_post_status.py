# Generated by Django 5.2.1 on 2025-06-03 23:2

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20250603_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='posts.status'),
            preserve_default=False,
        ),
    ]
