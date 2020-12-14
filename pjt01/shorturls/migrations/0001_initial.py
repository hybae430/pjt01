# Generated by Django 3.1.3 on 2020-12-11 06:09

from django.db import migrations, models
import shorturls.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True, validators=[shorturls.models.OptionalSchemeURLValidator()])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original', models.TextField(blank=True, null=True, validators=[shorturls.models.OptionalSchemeURLValidator()])),
                ('edit', models.TextField()),
                ('encoding', models.CharField(max_length=8)),
            ],
        ),
    ]