# Generated by Django 2.2.3 on 2019-08-02 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referrals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='referral',
            name='clicks',
            field=models.PositiveIntegerField(default=0),
        ),
    ]