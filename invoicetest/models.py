from django.db import models


class Invoice(models.Model):

    INVOICE_TYPE = [
        ("G", "Gotovina"),
        ("T", "Transakcijski račun"),
    ]

    invoice_number = models.CharField(max_length=128)
    invoice_date = models.DateField(auto_now=True)
    patient_name = models.CharField(max_length=128, blank=False, null=False)
    patient_surname = models.CharField(max_length=128, blank=True)
    patient_address = models.CharField(max_length=512, blank=True)
    invoice_type = models.CharField(max_length=20, choices=INVOICE_TYPE)

    def __str__(self):
        return self.invoice_number
    
class InvoiceData(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='articles', null=True, blank=True)
    article_name = models.CharField(max_length=128)
    article_price = models.FloatField()
    discount = models.FloatField(blank=True)
    number_of_articles = models.FloatField()

    def __str__(self):
        return self.invoice.invoice_number
