# Generated by Django 3.0.5 on 2020-05-30 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0004_auto_20200530_0844'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='enclosure',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='zoo.Enclosure'),
        ),
    ]
