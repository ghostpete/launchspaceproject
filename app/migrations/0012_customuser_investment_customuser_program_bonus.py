# Generated by Django 5.1.4 on 2025-03-09 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_payment_wallet_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='investment',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='Bonus'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='program_bonus',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='Bonus'),
        ),
    ]
