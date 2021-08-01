# Generated by Django 3.2.5 on 2021-07-28 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0009_alter_johannesburg_booking_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='johannesburg_booking',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]