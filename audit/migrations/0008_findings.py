# Generated by Django 4.0.1 on 2022-02-11 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0007_rename_dateeject_audit_dateexect'),
    ]

    operations = [
        migrations.CreateModel(
            name='findings',
            fields=[
                ('idFinding', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('idAudit', models.CharField(max_length=50)),
                ('alias', models.CharField(max_length=100)),
                ('detailFinding', models.CharField(max_length=500)),
                ('photoEvidence', models.ImageField(upload_to='')),
                ('docEvidence', models.BinaryField()),
            ],
        ),
    ]