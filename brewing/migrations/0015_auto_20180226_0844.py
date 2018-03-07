# Generated by Django 2.0.2 on 2018-02-26 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brewing', '0014_auto_20180222_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='transfer_cip',
            field=models.BooleanField(default=False, help_text='Tick this box if the container was cleaned prior to transfer.', verbose_name='CIP?'),
        ),
        migrations.AlterField(
            model_name='batch',
            name='ferm_tank',
            field=models.ForeignKey(default='', limit_choices_to={'container_type': 'F'}, on_delete=django.db.models.deletion.CASCADE, related_name='batch_ferm_tank', to='brewing.Container', verbose_name='Fermentation Tank'),
        ),
    ]