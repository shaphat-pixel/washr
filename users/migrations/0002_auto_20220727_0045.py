# Generated by Django 2.2.28 on 2022-07-27 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_order',
            old_name='picked_up',
            new_name='delivery_underway',
        ),
        migrations.RenameField(
            model_name='user_order',
            old_name='washed',
            new_name='doing_laundry',
        ),
        migrations.AddField(
            model_name='user_order',
            name='shirts_amount',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AddField(
            model_name='user_order',
            name='shorts_amount',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AddField(
            model_name='user_order',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='user_order',
            name='total_units',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AddField(
            model_name='user_order',
            name='trousers_amount',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AddField(
            model_name='user_order',
            name='verified',
            field=models.BooleanField(null=True),
        ),
    ]
