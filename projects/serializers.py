from rest_framework import serializers
from .models import Project         #la clase creada en projects/models.py
 
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields=('id','title','description','technology','created_at') #Los de la clase projects en projects/models.py
        read_only_fields=('created_at',)  #  Se indican cuales son de solo lectura 
                                          #importante la coma "," es para que lo lea como tupla