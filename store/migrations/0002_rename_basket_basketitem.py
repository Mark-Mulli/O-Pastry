# Generated by Django 4.0.4 on 2022-10-21 09:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_anonymoususer_last_name_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('seller', '0003_rename_orderpackage_order'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Basket',
            new_name='BasketItem',
        ),
    ]