# Generated by Django 4.0.1 on 2022-01-25 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0008_dpartment'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='student',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='age',
        ),
        migrations.AddField(
            model_name='student',
            name='Dpartment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='second_app.collage'),
        ),
        migrations.AlterModelTable(
            name='student',
            table=' Student',
        ),
    ]
