from iostestapi.models import Patient, PatientImages, PatientWorkText
from rest_framework import serializers


class PatientWorkTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientWorkText
        fields = "__all__"

class PatientImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientImages
        fields = "__all__"



class PatientSerializer(serializers.ModelSerializer):

    images = PatientImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False
    )

    work_text = PatientWorkTextSerializer(many=True, read_only=True)
    input_text = serializers.ListField(
        write_only=True,
        required=False
    )

    class Meta:
        model = Patient
        fields = ['id', 'name', 'surname', 'phone_number', 'patient_number', 'created_at', 'images', 'uploaded_images', 'work_text', 'input_text']


    
    def create(self, validated_data):
        if validated_data.get("uploaded_images") != None :
            uploaded_images = validated_data.pop("uploaded_images")
            input_text = validated_data.pop("input_text")
            patient = Patient.objects.create(**validated_data)

            for text in input_text:
                PatientWorkText.objects.create(patient=patient, work_text=text)

            for image in uploaded_images:
                PatientImages.objects.create(patient=patient, image=image)

            return patient
        else :
            input_text = validated_data.pop("input_text")
            patient = Patient.objects.create(**validated_data)

            for text in input_text:
                PatientWorkText.objects.create(patient=patient, work_text=text)

            return patient 
    """
    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        patient = Patient.objects.create(**validated_data)

        for image in uploaded_images:
            PatientImages.objects.create(patient=patient, image=image)

        return patient

    """

    def update(self, instance, validated_data):
        patient_image_list = validated_data.pop('uploaded_images')
        patient_work_text_list = validated_data.pop('input_text')
        instance.name = validated_data.get('name')
        instance.surname = validated_data.get('surname')
        instance.phone_number = validated_data.get('phone_number')
        instance.patient_number = validated_data.get('patient_number')
        instance.save()

        images_with_same_patient = PatientImages.objects.filter(patient=instance.pk).values_list('id', flat=True)

        images_id_pool = []

        for image in patient_image_list:
            """
            if "id" in image.keys():
                if PatientImages.objects.filter(id=image['id']).exists():
                    image_instance = PatientImages.objects.get(id=image['id'])
                    image_instance.save()
                    images_id_pool.append(image_instance.id)
                else:
                    continue
            else:
            """
            image_instance = PatientImages.objects.create(patient=instance, image=image)
            images_id_pool.append(image_instance.id)
            
        for image_id in images_with_same_patient:
            if image_id not in images_id_pool:
                PatientImages.objects.filter(pk=image_id).delete()

        for text in patient_work_text_list:
            text_instance = PatientWorkText.objects.create(patient=instance, work_text=text)
            text_instance.save()

        return instance
