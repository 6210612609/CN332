# Generated by Django 3.2.7 on 2022-03-15 06:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectBefore',
            fields=[
                ('status', models.BooleanField(choices=[('Approve', 'Approve'), ('Reject', 'Reject')], max_length=100)),
                ('ProID', models.AutoField(primary_key=True, serialize=False)),
                ('projectname', models.CharField(max_length=150)),
                ('projectmanager', models.CharField(max_length=150)),
                ('article', models.CharField(max_length=1500)),
                ('a', models.ManyToManyField(blank=True, related_name='AccID', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
