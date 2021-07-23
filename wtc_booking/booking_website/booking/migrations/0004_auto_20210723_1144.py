# Generated by Django 3.2.5 on 2021-07-23 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_venue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Johannesburg_booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, verbose_name='student name')),
                ('email', models.EmailField(max_length=250, verbose_name='email')),
                ('bootcamp_type', models.CharField(choices=[('LIVE', 'Live'), ('REMOTE', 'Remote')], default='Live', max_length=7, verbose_name='bootcamp_type')),
                ('bootcamp_month', models.CharField(max_length=10, verbose_name='bootcamp month')),
                ('camp_date', models.CharField(max_length=10, verbose_name='bootcamp date')),
            ],
        ),
        migrations.RenameModel(
            old_name='cpt_booking',
            new_name='Cape_Town_booking',
        ),
        migrations.RenameModel(
            old_name='booking',
            new_name='Durban_booking',
        ),
        migrations.DeleteModel(
            name='venue',
        ),
    ]
