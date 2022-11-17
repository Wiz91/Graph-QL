# Generated by Django 4.1.3 on 2022-11-16 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GraphQLapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NYC_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.CharField(max_length=20)),
                ('Address', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'NYC_data',
            },
        ),
    ]