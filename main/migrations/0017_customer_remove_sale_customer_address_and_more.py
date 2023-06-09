# Generated by Django 4.0.3 on 2023-05-20 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_sale_total_amt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(blank=True, default=' ', max_length=50)),
                ('customer_mobile', models.CharField(default=0, max_length=50)),
                ('customer_address', models.TextField(default=' ')),
            ],
        ),
        migrations.RemoveField(
            model_name='sale',
            name='customer_address',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='customer_mobile',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='customer_name',
        ),
        migrations.AddField(
            model_name='sale',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.customer'),
        ),
    ]
