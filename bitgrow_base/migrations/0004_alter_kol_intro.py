# Generated by Django 4.2.6 on 2023-10-15 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitgrow_base', '0003_alter_kol_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kol',
            name='intro',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='介绍'),
        ),
    ]
