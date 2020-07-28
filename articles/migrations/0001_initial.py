# Generated by Django 3.0.8 on 2020-07-24 08:43

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publication_date', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=250)),
                ('category', models.CharField(choices=[('новости', 'новости'), ('обучение', 'обучение')], max_length=100)),
                ('text', tinymce.models.HTMLField()),
                ('image', models.ImageField(default='articles/static/articles/image/cardimage.jpg', upload_to='')),
            ],
        ),
    ]