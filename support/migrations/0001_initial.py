# Generated by Django 4.1 on 2024-05-28 11:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service_requests', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SupportInteraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interaction_details', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('service_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service_requests.servicerequest')),
                ('support_rep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
