from django.shortcuts import render
from invoicetest import models
from rest_framework import viewsets
from invoicetest.models import Invoice
from invoicetest.serializer import InvoiceSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import filters

# Create your views here.

class InvoiceViewSet(viewsets.ModelViewSet):
    search_fields = ['invoice_number']
    filter_backends = (filters.SearchFilter,)
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    http_method_names = ['get','post','retrieve','put','patch','delete']
