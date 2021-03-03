# Generated by Django 3.1.6 on 2021-03-02 20:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0004_auto_20210227_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='cof_attack',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='cof_block',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='cof_dig',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='cof_rc',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='cof_serve',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='cof_set',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='total_attack',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='total_block',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='total_dig',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='total_rc',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='total_serve',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='total_set',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='zone',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(18)], verbose_name='Вага'),
        ),
    ]
