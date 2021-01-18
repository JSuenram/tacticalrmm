# Generated by Django 3.1.4 on 2021-01-18 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0001_initial'),
        ('clients', '0008_auto_20201103_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='alert_template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clients', to='alerts.alerttemplate'),
        ),
        migrations.AddField(
            model_name='site',
            name='alert_template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sites', to='alerts.alerttemplate'),
        ),
    ]
