# Generated by Django 2.1.5 on 2021-08-08 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=60)),
                ('synonym', models.CharField(default='', max_length=60)),
                ('antonym', models.CharField(default='', max_length=60)),
                ('partOfSpeech', models.CharField(default='', max_length=60)),
                ('meaning', models.CharField(default='', max_length=120)),
            ],
        ),
    ]
