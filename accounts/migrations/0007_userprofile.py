# Generated by Django 2.1 on 2019-06-28 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20190517_1250'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_usr', models.IntegerField()),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
    ]