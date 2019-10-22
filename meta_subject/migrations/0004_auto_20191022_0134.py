# Generated by Django 2.2.6 on 2019-10-21 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("meta_subject", "0003_auto_20191021_0534")]

    operations = [
        migrations.AlterModelOptions(
            name="historicalphysicalexam",
            options={
                "get_latest_by": "history_date",
                "ordering": ("-history_date", "-history_id"),
                "verbose_name": "historical Physical Exam",
            },
        ),
        migrations.AlterModelOptions(
            name="physicalexam",
            options={
                "verbose_name": "Physical Exam",
                "verbose_name_plural": "Physical Exams",
            },
        ),
    ]
