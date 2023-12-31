# Generated by Django 4.2.4 on 2023-08-30 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_snippet_is_public'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='snippet',
            name='tags',
            field=models.ManyToManyField(to='snippets.tag'),
        ),
    ]
