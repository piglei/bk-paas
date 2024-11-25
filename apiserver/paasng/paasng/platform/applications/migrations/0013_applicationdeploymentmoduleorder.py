# Generated by Django 4.2.16 on 2024-11-21 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0016_auto_20240904_1439'),
        ('applications', '0012_application_is_ai_agent_app'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationDeploymentModuleOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(verbose_name='顺序')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modules.module', unique=True, verbose_name='模块')),
            ],
            options={
                'verbose_name': '模块顺序',
            },
        ),
    ]
