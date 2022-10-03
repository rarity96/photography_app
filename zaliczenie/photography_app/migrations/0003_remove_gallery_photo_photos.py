# Generated by Django 4.1 on 2022-09-30 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("photography_app", "0002_profile_message_gallery_contact_availability"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="gallery",
            name="photo",
        ),
        migrations.CreateModel(
            name="Photos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "photo",
                    models.ImageField(blank=True, null=True, upload_to="images/post/"),
                ),
                (
                    "gallery",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="photography_app.gallery",
                    ),
                ),
            ],
        ),
    ]
