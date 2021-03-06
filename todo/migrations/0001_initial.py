# Generated by Django 3.2.9 on 2021-11-26 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=512)),
                ('priority', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
