# Generated by Django 4.1.5 on 2023-01-14 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phase1', '0011_alter_r1_1_d_alter_r1_1_l_alter_r1_1_no_alter_r1_1_w'),
    ]

    operations = [
        migrations.AlterField(
            model_name='r1_1',
            name='no',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
