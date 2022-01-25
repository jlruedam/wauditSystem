# Generated by Django 4.0.1 on 2022-01-24 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universe', '0009_universemanageresponsable_universeproces_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='universemacroproces',
            name='codeMacro',
            field=models.CharField(blank=True, max_length=5, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='universemanageresponsable',
            name='codeManage',
            field=models.CharField(blank=True, max_length=5, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='universeproces',
            name='codeProcess',
            field=models.CharField(blank=True, max_length=5, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='universeproces',
            name='responsable',
            field=models.CharField(max_length=100),
        ),
    ]