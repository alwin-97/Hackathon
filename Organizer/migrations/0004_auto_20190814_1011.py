# Generated by Django 2.1 on 2019-08-14 04:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Organizer', '0003_shareresource'),
    ]

    operations = [
        migrations.CreateModel(
            name='SponsorShip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(default=True, max_length=100)),
                ('platinum_sponsor', models.CharField(max_length=100)),
                ('f_platinum', models.TextField(max_length=1500)),
                ('ex_platinum', models.IntegerField()),
                ('gold_sponsor', models.CharField(max_length=100)),
                ('f_gold', models.TextField(max_length=1500)),
                ('ex_gold', models.IntegerField()),
                ('silver_sponsor', models.CharField(max_length=100)),
                ('f_silver', models.TextField(max_length=1500)),
                ('ex_silver', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SponsorShipDetails',
            fields=[
                ('event_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Organizer.EventDetails')),
                ('event_title', models.CharField(default=True, max_length=100)),
                ('platinum_sponsor', models.CharField(max_length=100)),
                ('f_platinum', models.TextField(max_length=1500)),
                ('ex_platinum', models.IntegerField()),
                ('gold_sponsor', models.CharField(max_length=100)),
                ('f_gold', models.TextField(max_length=1500)),
                ('ex_gold', models.IntegerField()),
                ('silver_sponsor', models.CharField(max_length=100)),
                ('f_silver', models.TextField(max_length=1500)),
                ('ex_silver', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='eventdetails',
            name='expected_participant',
            field=models.IntegerField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventdetails',
            name='org_id',
            field=models.ForeignKey(default=56, on_delete=django.db.models.deletion.CASCADE, to='Organizer.OrganiseEvent'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventdetails',
            name='us',
            field=models.ForeignKey(default=132, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organiseevent',
            name='event_description',
            field=models.CharField(default=1, max_length=800),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organiseevent',
            name='us',
            field=models.ForeignKey(default=131, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shareresource',
            name='org_id',
            field=models.ForeignKey(default=56, on_delete=django.db.models.deletion.CASCADE, to='Organizer.OrganiseEvent'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shareresource',
            name='us',
            field=models.ForeignKey(default=132, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='eventdetails',
            name='eligibility',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='eventdetails',
            name='event',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='eventdetails',
            name='event_detail_docs',
            field=models.FileField(upload_to='images/event_details_docs/'),
        ),
        migrations.AlterField(
            model_name='eventdetails',
            name='event_level',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='organiseevent',
            name='event_enddate',
            field=models.DateTimeField(default='2019-08-14 10:02:20.392972'),
        ),
        migrations.AlterField(
            model_name='organiseevent',
            name='event_poster',
            field=models.ImageField(blank=True, default='images/event_poster/Quotefancy-15975-3840x2160.jpg', upload_to='images/event_poster/'),
        ),
        migrations.AlterField(
            model_name='organiseevent',
            name='event_startdate',
            field=models.DateTimeField(default='2019-08-14 10:02:20.392972'),
        ),
        migrations.AlterField(
            model_name='shareresource',
            name='documentFile',
            field=models.FileField(upload_to='images/shared_resources_docs/'),
        ),
        migrations.AlterField(
            model_name='shareresource',
            name='resourceImage',
            field=models.ImageField(upload_to='images/shared_resources/'),
        ),
        migrations.AddField(
            model_name='sponsorshipdetails',
            name='org_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organizer.OrganiseEvent'),
        ),
        migrations.AddField(
            model_name='sponsorshipdetails',
            name='us',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sponsorship',
            name='org_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organizer.OrganiseEvent'),
        ),
        migrations.AddField(
            model_name='sponsorship',
            name='us',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]