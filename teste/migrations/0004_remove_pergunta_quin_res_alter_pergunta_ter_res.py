# Generated by Django 4.0.4 on 2022-05-26 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0003_rename_temas_tema'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pergunta',
            name='quin_res',
        ),
        migrations.AlterField(
            model_name='pergunta',
            name='ter_res',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]