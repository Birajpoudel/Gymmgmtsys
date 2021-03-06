# Generated by Django 4.0.4 on 2022-05-23 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_subplan_max_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanDiscout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_months', models.IntegerField()),
                ('total_discount', models.IntegerField()),
                ('subplan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.subplan')),
            ],
        ),
    ]
