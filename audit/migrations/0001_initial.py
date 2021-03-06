# Generated by Django 4.0.1 on 2022-02-07 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeAudit', models.CharField(max_length=25)),
                ('auditor', models.CharField(max_length=25)),
                ('zone', models.CharField(max_length=25)),
                ('deparment', models.CharField(max_length=25)),
                ('municipality', models.CharField(max_length=25)),
                ('codeAudit', models.CharField(max_length=10)),
                ('ambient', models.CharField(max_length=25)),
                ('ambientDetail', models.CharField(max_length=50)),
                ('datePlan', models.DateField()),
                ('ActDetail', models.CharField(max_length=500)),
            ],
        ),
    ]
