# Generated by Django 4.0.3 on 2022-04-20 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_project_options_project_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectcategory',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
