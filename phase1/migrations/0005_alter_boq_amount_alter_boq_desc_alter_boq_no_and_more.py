# Generated by Django 4.1.5 on 2023-01-14 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phase1', '0004_boq_delete_r1_1_delete_r2_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boq',
            name='amount',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='boq',
            name='desc',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='boq',
            name='no',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='boq',
            name='q',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='boq',
            name='rate',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='boq',
            name='unit',
            field=models.CharField(max_length=100),
        ),
    ]
