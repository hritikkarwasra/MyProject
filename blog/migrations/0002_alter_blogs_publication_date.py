# Generated by Django 4.2.2 on 2023-07-02 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='publication_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]