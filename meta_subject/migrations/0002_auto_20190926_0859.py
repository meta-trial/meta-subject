# Generated by Django 2.2.5 on 2019-09-26 05:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("meta_subject", "0001_initial")]

    operations = [
        migrations.RenameField(
            model_name="healtheconomics",
            old_name="higer_education",
            new_name="higher_education",
        ),
        migrations.RenameField(
            model_name="healtheconomics",
            old_name="higer_education_in_years",
            new_name="higher_education_in_years",
        ),
        migrations.RenameField(
            model_name="historicalhealtheconomics",
            old_name="higer_education",
            new_name="higher_education",
        ),
        migrations.RenameField(
            model_name="historicalhealtheconomics",
            old_name="higer_education_in_years",
            new_name="higher_education_in_years",
        ),
        migrations.AlterField(
            model_name="bloodresultsfbc",
            name="rbc",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=6,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1.0),
                    django.core.validators.MaxValueValidator(999999.0),
                ],
                verbose_name="Red blood cell count",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultslft",
            name="albumin_units",
            field=models.CharField(
                blank=True,
                choices=[("g/dL", "g/dL"), ("g/L", "g/L")],
                max_length=10,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsrft",
            name="creatinine",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=6,
                null=True,
                verbose_name="Creatinine",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsrft",
            name="urea",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=6,
                null=True,
                verbose_name="Urea (BUN)",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsrft",
            name="urea_units",
            field=models.CharField(
                blank=True,
                choices=[("mmol/L", "mmol/L")],
                max_length=10,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsrft",
            name="uric_acid",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=6,
                null=True,
                verbose_name="Uric Acid",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsfbc",
            name="rbc",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=6,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1.0),
                    django.core.validators.MaxValueValidator(999999.0),
                ],
                verbose_name="Red blood cell count",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultslft",
            name="albumin_units",
            field=models.CharField(
                blank=True,
                choices=[("g/dL", "g/dL"), ("g/L", "g/L")],
                max_length=10,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsrft",
            name="creatinine",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=6,
                null=True,
                verbose_name="Creatinine",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsrft",
            name="urea",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=6,
                null=True,
                verbose_name="Urea (BUN)",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsrft",
            name="urea_units",
            field=models.CharField(
                blank=True,
                choices=[("mmol/L", "mmol/L")],
                max_length=10,
                null=True,
                verbose_name="units",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsrft",
            name="uric_acid",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=6,
                null=True,
                verbose_name="Uric Acid",
            ),
        ),
    ]