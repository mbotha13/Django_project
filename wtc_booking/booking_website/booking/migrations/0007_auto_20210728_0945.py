# Generated by Django 3.2.5 on 2021-07-28 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_rename_name_johannesburg_booking_name_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='johannesburg_booking',
            name='name_id',
        ),
        migrations.AddField(
            model_name='johannesburg_booking',
            name='name',
            field=models.CharField(default='exit', max_length=55, verbose_name='student name'),
            preserve_default=False,
        ),
    ]
