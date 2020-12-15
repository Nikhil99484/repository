# Generated by Django 3.0 on 2020-02-02 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('price', models.FloatField(null=True)),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('description', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(choices=[('Indoor', 'Indoor'), ('Outdoor', 'Outdoor'), ('Anywhere', 'Anywhere')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Delivered', 'Delivered'), ('Pending', 'Pending'), ('Outfordelivery', 'Outfordelivery')], max_length=100)),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crmapp.Customers')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crmapp.Products')),
            ],
        ),
    ]
