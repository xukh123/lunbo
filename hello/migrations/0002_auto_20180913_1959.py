# Generated by Django 2.1.1 on 2018-09-13 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lunbo',
            fields=[
                ('id', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'imgs',
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
