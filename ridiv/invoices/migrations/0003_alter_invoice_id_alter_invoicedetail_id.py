# Generated by Django 5.0.1 on 2024-01-12 08:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("invoices", "0002_auto_20240112_1341"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invoice",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="invoicedetail",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
