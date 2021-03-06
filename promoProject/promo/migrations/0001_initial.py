# Generated by Django 3.1.4 on 2020-12-20 14:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import promo.helpers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
        ),
        migrations.CreateModel(
            name='NormalUser',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
        ),
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(choices=[('Percentage', 'percentage'), ('Points', 'points')], default='points', max_length=256)),
                ('code', models.CharField(default=promo.helpers.getPromoCode, editable=False, max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('amount', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='promo.normaluser')),
            ],
        ),
    ]
