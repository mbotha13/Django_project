# Generated by Django 3.2.5 on 2021-07-28 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_alter_johannesburg_booking_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='johannesburg_booking',
            old_name='name',
            new_name='name_id',
        ),
    ]
