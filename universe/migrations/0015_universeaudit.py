# Generated by Django 4.0.1 on 2022-01-31 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universe', '0014_remove_universemacroproces_nummacro_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniverseAudit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('numAudit', models.CharField(max_length=10)),
                ('generalAudit', models.CharField(max_length=25)),
                ('audit', models.CharField(max_length=100)),
                ('activities', models.CharField(max_length=100)),
                ('risk', models.CharField(max_length=100)),
                ('responsable', models.CharField(max_length=100)),
                ('macroProcess', models.CharField(max_length=100)),
                ('process', models.CharField(max_length=100)),
            ],
        ),
    ]
