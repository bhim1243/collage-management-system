# Generated by Django 5.0.3 on 2024-06-04 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collage_management_app', '0014_student_feedback_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_feedback',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
