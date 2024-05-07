# Generated by Django 5.0.4 on 2024-05-02 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]