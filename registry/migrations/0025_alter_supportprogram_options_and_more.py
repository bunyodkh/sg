# Generated by Django 5.2.3 on 2025-06-29 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0024_supportprogram_supportprogramtype_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='supportprogram',
            options={'ordering': ['name'], 'verbose_name': 'Support Program', 'verbose_name_plural': 'Support Programs'},
        ),
        migrations.AddField(
            model_name='supportprogramcycle',
            name='status',
            field=models.CharField(choices=[('upcoming', 'Upcoming'), ('ongoing', 'Ongoing'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='upcoming', help_text='Current status of the program cycle', max_length=50, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='supportprogram',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('archived', 'Archived')], default='active', help_text='Current status of the incubator program', max_length=50, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='supportprogramtype',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Type'),
        ),
    ]
