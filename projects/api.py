from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

#aqi indicareos que consultas se pueden hacer
class ProjectViewSet(viewsets.ModelViewSet):
    queryset=Project.objects.all()
    permission_classes=[permissions.AllowAny] #permite que todo consulte, #esto se puede cmabiar a los que esten autenticados                                         
    serializer_class= ProjectSerializer                                      