# Generated by Django 4.0.6 on 2022-07-30 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0004_rename_token_transcription'),
    ]

    operations = [
        migrations.AddField(
            model_name='transcription',
            name='tokens',
            field=models.JSONField(default=[]),
            preserve_default=False,
        ),
    ]