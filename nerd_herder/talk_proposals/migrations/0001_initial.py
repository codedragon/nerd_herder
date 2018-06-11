# Generated by Django 2.0.1 on 2018-06-11 05:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TalkProposal',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('talk_type', models.CharField(choices=[('full_length', 'Full Length (25+ minutes)'), ('lightning', 'Lightning Talk (5-10 minutes)')], max_length=64)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]