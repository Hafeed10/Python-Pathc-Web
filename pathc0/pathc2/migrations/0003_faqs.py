# Generated by Django 5.0.1 on 2024-02-19 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pathc2', '0002_promoter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faqs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('faq_type', models.CharField(choices=[('rent_tracking', 'Rent Tracking'), ('new_deposit', 'New_Deposit'), ('existing_deposit', 'Existing_Deposit')], max_length=128)),
            ],
        ),
    ]
