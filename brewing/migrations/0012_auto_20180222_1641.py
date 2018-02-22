# Generated by Django 2.0.2 on 2018-02-22 21:41

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.query_utils


class Migration(migrations.Migration):

    dependencies = [
        ('brewing', '0011_auto_20180222_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='transfer_tank',
            field=models.ForeignKey(blank=True, default='', limit_choices_to=django.db.models.query_utils.Q(('container_type', 'B'), ('container_type', 'A'), _connector='OR'), null=True, on_delete=django.db.models.deletion.CASCADE, to='brewing.Container', verbose_name='Transfer Tank'),
        ),
    ]
