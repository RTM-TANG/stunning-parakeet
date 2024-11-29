# Generated by Django 5.1.3 on 2024-11-28 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_remove_stock_price_item_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname_text', models.CharField(max_length=50)),
                ('description_text', models.CharField(default='', max_length=300)),
                ('features_text', models.CharField(default='', max_length=200)),
                ('deadline_date', models.DateTimeField(verbose_name='Deadline')),
                ('budget_float', models.FloatField(default=50)),
                ('username_text', models.CharField(max_length=50)),
                ('email_text', models.CharField(max_length=50)),
                ('contact_text', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
