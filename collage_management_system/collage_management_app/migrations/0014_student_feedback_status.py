# Generated by Django 5.0.3 on 2024-06-04 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collage_management_app', '0013_student_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_feedback',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
