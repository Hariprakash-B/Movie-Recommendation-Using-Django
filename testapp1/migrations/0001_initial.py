# Generated by Django 3.2 on 2021-05-14 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('item_id', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('timestamp', models.IntegerField()),
                ('title', models.CharField(max_length=50)),
            ],
        ),
    ]
