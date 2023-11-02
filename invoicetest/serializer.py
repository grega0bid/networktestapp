from rest_framework import serializers
from invoicetest.models import Invoice, InvoiceData


class InvoiceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceData
        fields = "__all__"


class InvoiceSerializer(serializers.ModelSerializer):

    articles = InvoiceDataSerializer(many=True)

    class Meta:
        model = Invoice
        fields = "__all__"

    def create(self, validated_data):
        articles = validated_data.pop("articles")
        invoice = Invoice.objects.create(**validated_data)

        for article in articles:
            InvoiceData.objects.create(invoice=invoice, **article)

        return invoice
    
    def update(self, instance, validated_data):
        articles_list = validated_data.pop('articles')
        instance.invoice_number = validated_data.get('invoice_number', instance.invoice_number)
        instance.patient_name = validated_data.get('patient_name', instance.patient_name)
        instance.patient_surname = validated_data.get('patient_surname', instance.patient_surname)
        instance.patient_address = validated_data.get('patient_address', instance.patient_address)
        instance.invoice_type = validated_data.get('invoice_type', instance.invoice_type)
        instance.save()

        articles_with_same_invoice = InvoiceData.objects.filter(invoice=instance.pk).values_list('id', flat=True)

        articles_id_pool = []

        for article in articles_list:
            article_instance = InvoiceData.objects.create(invoice=instance, **article)
            articles_id_pool.append(article_instance.id)

        for article_id in articles_with_same_invoice:
            if article_id not in articles_id_pool:
                InvoiceData.objects.filter(pk=article_id).delete()

        return instance
