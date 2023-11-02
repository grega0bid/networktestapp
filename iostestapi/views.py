from iostestapi.models import Patient
from rest_framework import viewsets
from rest_framework import permissions
from iostestapi.serializer import PatientSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.generics import CreateAPIView
from rest_framework import filters


class PatientViewSet(viewsets.ModelViewSet):
    search_fields = ['work_text__id']
    filter_backends = (filters.SearchFilter,)
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get','post','retrieve','put','patch','delete']


"""
class PatientCreateView(CreateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = PatientSerializer

"""