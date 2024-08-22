# Generated by Django 5.1 on 2024-08-22 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_text', models.TextField()),
                ('source_lang_slug', models.CharField(default='', max_length=5)),
                ('target_lang_slug', models.CharField(default='', max_length=5)),
                ('translated_text', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
