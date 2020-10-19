# Generated by Django 2.1.2 on 2019-02-13 16:25

from django.db import migrations, models
import django.db.models.deletion
import economy.models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_auto_20190209_1216'),
        ('kudos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransferEnabledFor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transfers_enabled', to='dashboard.Profile')),
                ('token', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transfers_enabled', to='kudos.Token')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]