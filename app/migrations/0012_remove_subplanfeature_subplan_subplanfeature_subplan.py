# Generated by Django 4.0.4 on 2022-05-18 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_subplanfeature_alter_subplan_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subplanfeature',
            name='subplan',
        ),
        migrations.AddField(
            model_name='subplanfeature',
            name='subplan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.subplan'),
        ),
    ]
