# Generated by Django 5.2.3 on 2025-07-11 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0002_startup_operation_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='show_on_website',
            field=models.BooleanField(default=True, help_text='Show organization on the organization explore page.', verbose_name='Show on Website'),
        ),
    ]
