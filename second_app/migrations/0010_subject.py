# Generated by Django 4.0.1 on 2022-01-25 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0009_alter_student_managers_remove_student_age_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_practical', models.BooleanField(default=False)),
                ('total_marks', models.IntegerField()),
            ],
            options={
                'db_table': ' sunject',
            },
        ),
    ]