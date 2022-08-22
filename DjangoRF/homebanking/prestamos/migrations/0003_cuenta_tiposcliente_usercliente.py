# Generated by Django 4.1 on 2022-08-14 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0002_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('account_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_id', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('iban', models.TextField()),
                ('tipo_cuenta', models.IntegerField()),
            ],
            options={
                'db_table': 'cuenta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TiposCliente',
            fields=[
                ('tipo_cliente_id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_cliente', models.TextField()),
            ],
            options={
                'db_table': 'tipos_cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField()),
                ('id_cliente', models.IntegerField()),
            ],
            options={
                'db_table': 'user_cliente',
                'managed': False,
            },
        ),
    ]
