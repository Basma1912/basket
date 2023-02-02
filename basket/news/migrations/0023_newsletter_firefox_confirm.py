# Generated by Django 2.2.17 on 2021-03-25 19:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0022_delete_transactionalemailmessage"),
    ]

    operations = [
        migrations.AddField(
            model_name="newsletter",
            name="firefox_confirm",
            field=models.BooleanField(
                default=False,
                help_text="Whether to send the Firefox or Mozilla branded confirmation message for this newsletter",
            ),
        ),
    ]
