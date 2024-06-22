from modules.apps import ModulesConfig
from rest_framework.routers import DefaultRouter
from modules.views import ModuleViewSet


app_name = ModulesConfig.name
router = DefaultRouter()
router.register(r'module', ModuleViewSet, basename='module')

urlpatterns = [

] + router.urls
