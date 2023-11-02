from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    patient_number = models.IntegerField()

    def __str__(self):
        return self.name
    
class PatientImages(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='images')
    image_description = models.CharField(max_length=64)
    image = models.ImageField(upload_to="rtgs", blank=True, null=True)

    def __str__(self):
        return "%s" % (self.patient.name)

class PatientWorkText(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="work_text")
    date_of_visit = models.DateTimeField(auto_now=True)
    work_text = models.TextField()