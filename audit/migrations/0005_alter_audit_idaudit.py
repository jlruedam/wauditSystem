# Generated by Django 4.0.1 on 2022-02-08 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0004_alter_audit_codeaudit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audit',
            name='idAudit',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]