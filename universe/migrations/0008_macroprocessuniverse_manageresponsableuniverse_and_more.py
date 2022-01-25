# Generated by Django 4.0.1 on 2022-01-24 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universe', '0007_alter_persona_id_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='MacroprocessUniverse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('macroprocess', models.CharField(max_length=100)),
                ('responsable', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='manageResponsableUniverse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsable', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProcesesUniverse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsable', models.CharField(max_length=100, null=True)),
                ('macroprocess', models.CharField(max_length=100)),
                ('process', models.CharField(max_length=100)),
            ],
        ),
    ]
