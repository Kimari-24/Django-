from rest_framework.routers import DefaultRouter

from .views import ClientesViewSet


router = DefaultRouter()
router.register('', ClientesViewSet, basename='cliente')

urlpatterns = router.urls