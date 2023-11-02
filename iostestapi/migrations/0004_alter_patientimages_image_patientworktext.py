# Generated by Django 4.2.1 on 2023-06-28 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iostestapi', '0003_alter_patientimages_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientimages',
            name='image',
            field=models.ImageField(blank=True, upload_to='rtgs'),
        ),
        migrations.CreateModel(
            name='PatientWorkText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_visit', models.DateTimeField(auto_now=True)),
                ('work_text', models.TextField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_text', to='iostestapi.patient')),
            ],
        ),
    ]