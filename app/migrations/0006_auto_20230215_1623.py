# Generated by Django 3.0 on 2023-02-15 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20230215_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='competition_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.competition'),
        ),
    ]
