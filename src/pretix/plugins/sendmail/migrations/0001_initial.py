# Generated by Django 3.2.2 on 2021-06-03 09:17

import django.db.models.deletion
import i18nfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pretixbase', '0191_event_last_modified'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('subject', i18nfield.fields.I18nCharField(max_length=255)),
                ('template', i18nfield.fields.I18nTextField()),
                ('all_products', models.BooleanField(default=True)),
                ('include_pending', models.BooleanField(default=False)),
                ('send_date', models.DateTimeField(blank=True, null=True)),
                ('send_offset_days', models.IntegerField(null=True)),
                ('send_offset_time', models.TimeField(blank=True, null=True)),
                ('date_is_absolute', models.BooleanField(default=True)),
                ('offset_to_event_end', models.BooleanField(default=False)),
                ('offset_is_after', models.BooleanField(default=False)),
                ('send_to', models.CharField(default='orders', max_length=10)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sendmail_rules', to='pretixbase.event')),
                ('limit_products', models.ManyToManyField(to='pretixbase.Item')),
            ],
        ),
        migrations.CreateModel(
            name='ScheduledMail',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('last_computed', models.DateTimeField(auto_now_add=True)),
                ('computed_datetime', models.DateTimeField(db_index=True)),
                ('state', models.CharField(default='scheduled', max_length=100)),
                ('last_successful_order_id', models.BigIntegerField(null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pretixbase.event')),
                ('rule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sendmail.rule')),
                ('subevent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pretixbase.subevent')),
            ],
            options={
                'unique_together': {('rule', 'subevent')},
            },
        ),
    ]
