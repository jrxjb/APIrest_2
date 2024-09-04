from rest_framework import routers
from .api import ProjectViewSet

router= routers.DefaultRouter()
router.register('api/projects',ProjectViewSet,'projects')
urlpatterns = router.urls
 

#'api/projects' Es el nombre de la ruta
#Esta basado en el conjunto de datos de ProjectsViewsSet
#El nomabre es projects

#exportamos un urlpatterns

#Con todo Esto el maneja las peticiones