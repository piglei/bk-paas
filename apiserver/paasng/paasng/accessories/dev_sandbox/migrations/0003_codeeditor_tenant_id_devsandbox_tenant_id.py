# Generated by Django 4.2.17 on 2025-01-17 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dev_sandbox", "0002_rename_expire_at_devsandbox_expired_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="codeeditor",
            name="tenant_id",
            field=models.CharField(
                db_index=True,
                default="default",
                help_text="本条数据的所属租户",
                max_length=32,
                verbose_name="租户 ID",
            ),
        ),
        migrations.AddField(
            model_name="devsandbox",
            name="tenant_id",
            field=models.CharField(
                db_index=True,
                default="default",
                help_text="本条数据的所属租户",
                max_length=32,
                verbose_name="租户 ID",
            ),
        ),
    ]