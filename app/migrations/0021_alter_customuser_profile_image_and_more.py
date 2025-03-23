# Generated by Django 5.1.4 on 2025-03-23 21:38

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_kyc_image_holding_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='kyc',
            name='back_id_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='kyc',
            name='front_id_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='kyc',
            name='image_holding_id',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='kyc',
            name='proof_of_employment',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='kyc',
            name='proof_of_income',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='confirmation_receipt',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='support',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
    ]
