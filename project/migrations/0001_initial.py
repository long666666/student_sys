# Generated by Django 3.2.13 on 2022-05-11 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=32)),
                ('first_day', models.DateField()),
            ],
            options={
                'db_table': 'class',
            },
        ),
    ]
