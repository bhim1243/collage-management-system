# Generated by Django 5.0.3 on 2024-06-03 03:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collage_management_app', '0011_staff_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('massage', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(default=0, null=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collage_management_app.student')),
            ],
        ),
    ]
