# Generated by Django 3.2.4 on 2021-06-26 17:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='歩数')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新日時')),
            ],
            options={
                'verbose_name': 'step',
                'verbose_name_plural': 'steps',
            },
        ),
    ]
